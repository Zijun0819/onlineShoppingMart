$(function () {
    var $slides = $('.slide_pics li');
    var len = $slides.length;
    var nowli = 0;
    var prevli = 0;
    var $prev = $('.prev');
    var $next = $('.next');
    var ismove = false;
    var timer = null;

    // 初始化轮播图位置
    $slides.not(':first').css({ left: 760 });

    // 动态生成小圆点
    var $pointsContainer = $('.points');
    $pointsContainer.empty(); // 避免重复生成小圆点
    for (let i = 0; i < len; i++) {
        var $li = $('<li>');
        if (i === 0) $li.addClass('active');
        $li.appendTo($pointsContainer);
    }

    let $points = $('.points li'); // 更新选择器引用

    // 自动播放定时器
    timer = setInterval(autoplay, 3000);

    // 鼠标悬停时暂停轮播
    $('.slide').hover(
        function () {
            clearInterval(timer);
        },
        function () {
            timer = setInterval(autoplay, 3000);
        }
    );

    function autoplay() {
        nowli++;
        if (nowli >= len) nowli = 0; // 防止超出索引范围
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    }

    $points.click(function () {
        if (ismove) return;

        nowli = $(this).index(); // 获取当前点击的小圆点索引
        if (nowli === prevli) return; // 防止重复点击

        $(this).addClass('active').siblings().removeClass('active');
        move();
    });

    $prev.click(function () {
        if (ismove) return;

        nowli--;
        if (nowli < 0) nowli = len - 1; // 防止索引小于0
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    });

    $next.click(function () {
        if (ismove) return;

        nowli++;
        if (nowli >= len) nowli = 0; // 防止索引超出范围
        move();
        $points.eq(nowli).addClass('active').siblings().removeClass('active');
    });

    function move() {
        ismove = true;

        // 判断移动方向
        let direction = nowli > prevli || (nowli === 0 && prevli === len - 1) ? 760 : -760;
        let reverseDirection = -direction;

        // 初始化当前项的位置
        $slides.eq(nowli).css({ left: direction });

        // 动画效果
        $slides.eq(prevli).animate({ left: reverseDirection }, 800, 'easeOutExpo');
        $slides.eq(nowli).animate({ left: 0 }, 800, 'easeOutExpo', function () {
            ismove = false; // 动画结束后解除锁定
        });

        // 更新上一个索引
        prevli = nowli;
    }
});
