// The language switch is a native <details>. All this adds is the part the
// browser will not do: close the open one when the click lands elsewhere, and
// on Escape.
document.addEventListener('click', function (e) {
  document.querySelectorAll('details.lang[open]').forEach(function (d) {
    if (!d.contains(e.target)) d.open = false;
  });
});
document.addEventListener('keydown', function (e) {
  if (e.key !== 'Escape') return;
  document.querySelectorAll('details.lang[open]').forEach(function (d) { d.open = false; });
});
