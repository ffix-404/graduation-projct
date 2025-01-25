document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header")
    const scrollElements = document.querySelectorAll(".fade-in, .scale-in, .slide-in-left, .slide-in-right")
  
    const elementInView = (el, percentageScroll = 100) => {
      const elementTop = el.getBoundingClientRect().top
      return elementTop <= (window.innerHeight || document.documentElement.clientHeight) * (percentageScroll / 100)
    }
  
    const displayScrollElement = (element) => {
      element.classList.add("visible")
    }
  
    const hideScrollElement = (element) => {
      element.classList.remove("visible")
    }
  
    const handleScrollAnimation = () => {
      scrollElements.forEach((el) => {
        if (elementInView(el, 75)) {
          displayScrollElement(el)
        } else {
          hideScrollElement(el)
        }
      })
    }
  
    // Sticky header
    const stickyHeader = () => {
      if (window.scrollY > 0) {
        header.classList.add("sticky")
      } else {
        header.classList.remove("sticky")
      }
    }
  
    // Throttle function to limit the rate at which a function can fire
    const throttle = (fn, wait) => {
      let time = Date.now()
      return () => {
        if (time + wait - Date.now() < 0) {
          fn()
          time = Date.now()
        }
      }
    }
  
    window.addEventListener(
      "scroll",
      throttle(() => {
        handleScrollAnimation()
        stickyHeader()
      }, 100),
    )
  
    // Initial check for elements in view
    handleScrollAnimation()
  })
  
  
