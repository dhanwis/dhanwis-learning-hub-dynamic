function handleIntersection(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      } else {
        entry.target.classList.remove('active');
      }
    });
  }

  const observer = new IntersectionObserver(handleIntersection, { threshold: 0.5 });

  document.querySelectorAll('.fadeInUp, .zoomIn, .fadeRight, .fadeLeft, .flipRight, .flipLeft').forEach(element => {
    observer.observe(element);
  });


  //////////////////////////////////////////////////////////////////////////////////////////////////////////

  /* for current page active */


  // Get the current page URL
  var currentPage = window.location.href;

  // Get all the links in the navigation menu
  var menuLinks = document.querySelectorAll('.main-menu-3 ul li a');

  // Loop through each link and check if its href matches the current page URL
  for (var i = 0; i < menuLinks.length; i++) {
    var link = menuLinks[i];

    // Compare the href of the link with the current page URL
    if (link.href === currentPage) {
      // If there's a match, add the "active" class to the link
      link.classList.add('active');
    }
  }


  /////////////////// for mobile active  ////////////////////


  // Get the current page URL
  var currentPage = window.location.href;

  // Get all the links in the navigation menu
  var menuLinks = document.querySelectorAll('.mean-container .mean-nav ul li a');

  // Loop through each link and check if its href matches the current page URL
  for (var i = 0; i < menuLinks.length; i++) {
    var link = menuLinks[i];

    // Compare the href of the link with the current page URL
    if (link.href === currentPage) {
      // If there's a match, add the "active" class to the link
      link.classList.add('active');
    }
  }