// Automatically add target="_blank" and rel="noopener noreferrer" to external links
document.addEventListener('DOMContentLoaded', function() {
  // Get all links in the content area
  const links = document.querySelectorAll('.md-content a[href^="http"]');

  links.forEach(function(link) {
    const href = link.getAttribute('href');

    // Skip localhost and 127.0.0.1
    if (href && !href.includes('localhost') && !href.includes('127.0.0.1')) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});
