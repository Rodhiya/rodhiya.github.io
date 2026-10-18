// Filter buttons for the Creative Space page.
// The selected category is kept in the URL hash (e.g. /creative/#poems), so a
// post's tag can link straight to a filtered list.
(function() {
  var buttons = document.querySelectorAll('.creative-filter');
  var items = document.querySelectorAll('.creative-item');
  if (!buttons.length) return;

  function applyFilter(filter) {
    var known = Array.prototype.some.call(buttons, function(b) { return b.dataset.filter === filter; });
    if (!known) filter = 'all';

    buttons.forEach(function(b) {
      var active = b.dataset.filter === filter;
      b.classList.toggle('active', active);
      b.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    items.forEach(function(item) {
      item.hidden = filter !== 'all' && item.dataset.category !== filter;
    });
  }

  buttons.forEach(function(b) {
    b.addEventListener('click', function() {
      var filter = b.dataset.filter;
      history.replaceState(null, '', filter === 'all' ? location.pathname : '#' + filter);
      applyFilter(filter);
    });
  });

  window.addEventListener('hashchange', function() { applyFilter(location.hash.slice(1)); });
  applyFilter(location.hash.slice(1));
})();
