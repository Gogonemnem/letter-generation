// Countdown timer logic
function startTimer(duration, display) {
    var timer = duration, seconds;
    var end = setInterval(function () {
        seconds = parseInt(timer, 10);

        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = seconds + " seconds remaining";

        if (--timer < 0) {
            clearInterval(end);
            display.textContent = "Time's up!";
        }
    }, 1000);
}

// Keydown event for spacebar to submit the form
document.body.addEventListener('keydown', function(event) {
    if (event.keyCode === 32) {
        event.preventDefault();
        document.getElementById('new-letter-form').submit();
    }
});

// Page load event to start the countdown timer and check max score
window.addEventListener('load', function() {
    var thirtySeconds = 30,
        display = document.querySelector('#timer');
    startTimer(thirtySeconds, display);

    var maxScoreReached = JSON.parse(document.querySelector('#max-score-reached').textContent);
    var modal = document.getElementById('celebration-modal');
    var closeModal = document.getElementById('close-modal');

    if (maxScoreReached) {
        modal.style.display = 'block';
    }

    closeModal.onclick = function() {
        modal.style.display = 'none';
    };
});
