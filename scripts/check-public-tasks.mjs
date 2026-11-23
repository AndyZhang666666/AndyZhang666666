// Run with Playwright and its Chromium browser installed. Set BROWSER_CHANNEL=chrome to use Chrome.
import assert from 'node:assert/strict';
import { chromium } from 'playwright';
import { readFile } from 'node:fs/promises';

const site = 'https://andyzhang666666.github.io';
const entries = [
  '/llm-output-eval/?sample=e06&dimension=structure',
  '/growth-experiment-lab/#read',
  '/bundle-lab/simulate/',
];
for (const name of ['README.md', 'README.en.md']) {
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
  await page.getByText('暂不全量，仍有条件待核对', { exact: true }).waitFor();
  assert(await page.getByText(/p = 0.0492/).first().isVisible());
  assert(await page.getByLabel(/预设最低业务提升/).isVisible());
  const guardrail = page.getByLabel(/留存、退款、投诉与成本护栏/);
  await guardrail.selectOption('fail');
  assert.equal(await guardrail.inputValue(), 'fail');

  await page.goto(site + entries[2]);
  const discount = page.getByRole('spinbutton', { name: '套餐折扣率数值' });
  for (const [percent, margin] of [[6, '13.44'], [8, '-7.54']]) {
    await discount.fill(String(percent));
    await discount.press('Tab');
    const result = page.getByText('当前草稿 · 增量毛利', { exact: true }).locator('..');
    await result.getByText('¥' + margin, { exact: true }).waitFor();
  }
  assert.deepEqual(writes, []);
  console.log('Passed: cited source, synthetic rollout decision, and two discount scenarios.');
} finally {
  await browser.close();
}
