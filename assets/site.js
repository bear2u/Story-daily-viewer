const search = document.querySelector('[data-search]');
const filters = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('[data-story]')];
let category = 'all';
function applyFilters() {
  const query = (search?.value || '').trim().toLocaleLowerCase('ko');
  let visible = 0;
  cards.forEach(card => {
    const match = (category === 'all' || card.dataset.tags.split('|').includes(category)) && card.dataset.search.toLocaleLowerCase('ko').includes(query);
    card.hidden = !match;
    if (match) visible++;
  });
  const empty = document.querySelector('[data-empty]');
  if (empty) empty.hidden = visible > 0;
  const count = document.querySelector('[data-visible-count]');
  if (count) count.textContent = visible;
}
search?.addEventListener('input', applyFilters);
filters.forEach(button => button.addEventListener('click', () => {
  category = button.dataset.filter;
  filters.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
  applyFilters();
}));
document.querySelector('[data-reset]')?.addEventListener('click', () => {
  if (search) search.value = '';
  category = 'all';
  filters.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === 'all')));
  applyFilters();
  search?.focus();
});
const progress = document.querySelector('.reading-progress');
function updateProgress() {
  const maximum = document.documentElement.scrollHeight - innerHeight;
  if (progress) progress.style.width = `${maximum > 0 ? Math.min(100,scrollY / maximum * 100) : 100}%`;
  const top = document.querySelector('[data-top]');
  if (top) top.hidden = scrollY < 500;
}
addEventListener('scroll', updateProgress, {passive:true});
addEventListener('resize', updateProgress);
updateProgress();
document.querySelector('[data-top]')?.addEventListener('click', () => scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}));
const dialog = document.querySelector('.image-dialog');
document.querySelectorAll('[data-zoom]').forEach(button => button.addEventListener('click', () => {
  if (!dialog) return;
  const image = button.querySelector('img');
  const large = dialog.querySelector('img');
  large.src = image.src;
  large.alt = image.alt;
  dialog.querySelector('.dialog-caption').textContent = image.alt;
  dialog.showModal();
}));
dialog?.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog?.addEventListener('click', e => {if (e.target === dialog) dialog.close();});
const anchors = [...document.querySelectorAll('.toc a')];
if ('IntersectionObserver' in window && anchors.length) {
  const observer = new IntersectionObserver(entries => {
    const entry = entries.find(item => item.isIntersecting);
    if (!entry) return;
    anchors.forEach(a => a.classList.toggle('active', a.hash === `#${entry.target.id}`));
  }, {rootMargin:'-12% 0px -65% 0px'});
  document.querySelectorAll('.part[id]').forEach(part => observer.observe(part));
}

// Load the YouTube player only after the visitor presses Play.
document.querySelectorAll('[data-youtube]').forEach(button => button.addEventListener('click', () => {
  const videoId = button.dataset.youtube;
  if (!/^[A-Za-z0-9_-]{11}$/.test(videoId)) return;
  const player = document.createElement('iframe');
  player.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&playsinline=1&rel=0`;
  player.title = `${button.dataset.videoTitle} · YouTube 영상`;
  player.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen';
  player.allowFullscreen = true;
  player.referrerPolicy = 'strict-origin-when-cross-origin';
  button.replaceWith(player);
  player.focus();
}));
