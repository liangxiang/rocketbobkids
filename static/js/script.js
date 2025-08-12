// 主页面JavaScript功能

document.addEventListener('DOMContentLoaded', function() {
    // 添加页面加载动画
    initPageAnimations();
    
    // 初始化平滑滚动
    initSmoothScroll();
    
    // 初始化工具提示
    initTooltips();
    
    // 添加导航栏滚动效果
    initNavbarScroll();
});

// 页面动画初始化
function initPageAnimations() {
    // 为卡片添加延迟动画
    const cards = document.querySelectorAll('.bg-white.rounded-xl');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.animation = `slideInUp 0.6s ease-out forwards`;
        card.style.animationDelay = `${index * 0.2}s`;
    });

    // 为特性图标添加悬停动画
    const icons = document.querySelectorAll('.fas, .fab');
    icons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });
}

// 平滑滚动初始化
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// 工具提示初始化
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(e) {
    const tooltip = e.target.getAttribute('data-tooltip');
    if (tooltip) {
        e.target.classList.add('tooltip-visible');
    }
}

function hideTooltip(e) {
    e.target.classList.remove('tooltip-visible');
}

// 导航栏滚动效果
function initNavbarScroll() {
    const navbar = document.querySelector('nav');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 1)';
            navbar.style.backdropFilter = 'none';
            navbar.style.boxShadow = '0 1px 3px 0 rgba(0, 0, 0, 0.1)';
        }
        
        lastScrollY = currentScrollY;
    });
}

// PDF查看器相关功能
class PDFViewer {
    constructor() {
        this.isFullscreen = false;
        this.initEventListeners();
    }
    
    initEventListeners() {
        // 全屏切换
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isFullscreen) {
                this.exitFullscreen();
            }
        });
        
        // 监听全屏变化
        document.addEventListener('fullscreenchange', () => {
            this.isFullscreen = !!document.fullscreenElement;
        });
    }
    
    toggleFullscreen() {
        const embed = document.getElementById('pdf-embed');
        if (!this.isFullscreen) {
            this.enterFullscreen(embed);
        } else {
            this.exitFullscreen();
        }
    }
    
    enterFullscreen(element) {
        if (element.requestFullscreen) {
            element.requestFullscreen();
        } else if (element.webkitRequestFullscreen) {
            element.webkitRequestFullscreen();
        } else if (element.mozRequestFullScreen) {
            element.mozRequestFullScreen();
        } else if (element.msRequestFullscreen) {
            element.msRequestFullscreen();
        }
    }
    
    exitFullscreen() {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
    }
}

// 实用工具函数
const Utils = {
    // 防抖函数
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // 节流函数
    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },
    
    // 显示通知
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 text-white ${
            type === 'success' ? 'bg-green-500' : 
            type === 'error' ? 'bg-red-500' : 
            type === 'warning' ? 'bg-yellow-500' : 'bg-blue-500'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // 动画进入
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
            notification.style.opacity = '1';
        }, 100);
        
        // 自动消失
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            notification.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
};

// 初始化PDF查看器
if (document.getElementById('pdf-embed')) {
    const pdfViewer = new PDFViewer();
    window.toggleFullscreen = () => pdfViewer.toggleFullscreen();
}

// 性能监控
const Performance = {
    startTime: Date.now(),
    
    logPageLoad() {
        window.addEventListener('load', () => {
            const loadTime = Date.now() - this.startTime;
            console.log(`页面加载时间: ${loadTime}ms`);
        });
    }
};

Performance.logPageLoad();