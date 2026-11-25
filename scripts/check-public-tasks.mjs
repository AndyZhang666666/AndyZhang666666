// Run with Playwright and its Chromium browser installed. Set BROWSER_CHANNEL=chrome to use Chrome.
import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { readFile } from 'node:fs/promises';

const site = 'https://andyzhang666666.github.io';
const entries = [
  '/llm-output-eval/?sample=e06&dimension=structure',
  '/agent-bench/',
  '/rag-lab/',
  '/bundle-lab/simulate/',
  '/growth-experiment-lab/#read',
];
for (const name of ['README.md', 'README.en.md', 'README.zh-CN.md']) {
  const markdown = await readFile(new URL('../' + name, import.meta.url), 'utf8');
  let previous = -1;
  for (const path of entries) {
    const position = markdown.indexOf('](' + site + path + ')');
    assert(position > previous, name + ' is missing an ordered task link: ' + path);
    previous = position;
  }
}

const browser = await chromium.launch({ channel: process.env.BROWSER_CHANNEL || undefined });
try {
  const context = await browser.newContext({ serviceWorkers: 'block' });
  const writes = [];
  await context.route('**/*', route => {
    const method = route.request().method();
    if (['GET', 'HEAD', 'OPTIONS'].includes(method)) return route.continue();
    writes.push(method);
    return route.abort();
  });
  const page = await context.newPage();
  await page.goto(site + entries[0]);
  await page.getByRole('button', { name: /定位到原文/ }).click();
  const quote = page.locator('mark').filter({ hasText: '他看清了那人胸牌上的' }).first();
  await quote.waitFor({ state: 'visible' });
  assert(await quote.evaluate(el => {
    const rect = el.getBoundingClientRect();
    return rect.bottom > 0 && rect.top < innerHeight;
  }), 'The cited source must be in the viewport');
  assert.match(await page.locator('body').innerText(), /结构完整性\n核对评分档 ↓\n2\/5/);

  await page.goto(site + entries[1]);
  await page.locator('button[data-case="timeout"]').click();
  await page.locator('#finish').click();
  const verdict = page.locator('#verdict');
  await verdict.waitFor();
  assert.equal(await verdict.locator('.recap-card').count(), 2);
  assert.match(await verdict.innerText(), /条跟进记录/);
  assert.match(await verdict.innerText(), /程序案例/);

  await page.goto(site + entries[2]);
  const source = page.locator('#sources');
  await source.getByText(/14/).first().waitFor();
  const settings = page.locator('#conditionSettings');
  if (!await settings.evaluate(el => el.open)) await settings.locator('summary').click();
  await page.locator('#date').fill('2026-06-30');
  await page.locator('#date').press('Tab');
  await page.locator('#stale').waitFor();
  await page.locator('#staleRerun').click();
  await source.getByText(/30/).first().waitFor();
  assert.match(await page.locator('#runScope').innerText(), /2026-06-30/);

  await page.goto(site + entries[4]);
  await page.getByText('暂不全量，仍有条件待核对', { exact: true }).waitFor();
  assert(await page.getByText(/p = 0.0492/).first().isVisible());
  assert(await page.getByLabel(/预设最低业务提升/).isVisible());
  const guardrail = page.getByLabel(/留存、退款、投诉与成本护栏/);
  await guardrail.selectOption('fail');
  assert.equal(await guardrail.inputValue(), 'fail');

  await page.goto(site + entries[3]);
  const discount = page.getByRole('spinbutton', { name: '套餐折扣率数值' });
  for (const [percent, margin] of [[6, '13.44'], [8, '-7.54']]) {
    await discount.fill(String(percent));
    await discount.press('Tab');
    const result = page.getByText('当前草稿 · 增量毛利', { exact: true }).locator('..');
    await result.getByText('¥' + margin, { exact: true }).waitFor();
  }
  assert.deepEqual(writes, []);
  console.log('Passed: quote review, lost-response replay, date-scoped retrieval, rollout guardrails and discount ledger.');
} finally {
  await browser.close();
}
