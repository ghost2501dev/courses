let scrollToTopBtn = document.getElementById('scroll-to-top')
scrollToTopBtn.onclick = scrollToTop

window.onscroll = function() {
  showHideScrollToTopBtn()
}

function showHideScrollToTopBtn() {
  if (document.documentElement.scrollTop > 50 || document.body.scrollTop > 50 ) {
    scrollToTopBtn.style.display = 'block'
  } else {
    scrollToTopBtn.style.display = 'none'
  }
}

function scrollToTop() {
  document.body.scrollTop = 0  // For Safari
  document.documentElement.scrollTop = 0
}

