document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add mobile menu functionality


const header = document.querySelector('header');
const nav = document.querySelector('nav');

header.insertBefore(mobileMenuButton, nav);

mobileMenuButton.addEventListener('click', () => {
    nav.classList.toggle('active');
});

// Add intersection observer for fade-in animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('section').forEach(section => {
    section.classList.add('fade-in');
    observer.observe(section);
});

// Add hover effects for project cards
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.querySelector('.project-content').style.transform = 'translateY(0)';
    });

    card.addEventListener('mouseleave', () => {
        card.querySelector('.project-content').style.transform = 'translateY(100%)';
    });
});