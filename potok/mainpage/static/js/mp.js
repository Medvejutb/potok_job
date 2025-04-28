document.addEventListener("DOMContentLoaded", function () {
    const popups = document.querySelectorAll(".popa");
    const infBlocks = document.querySelectorAll('[id^="inf"]');
    const closeButtons = document.querySelectorAll(".close");

    function hidePopup() {
        popups.forEach((popup) => {
            popup.style.display = "none";
            const content = popup.querySelector(".popup-content");
            if (content) content.innerHTML = "";
        });
    }

    function showPopup(popup, url) {
        hidePopup();
        popup.style.display = "block";

        fetch(url)
            .then((response) => response.text())
            .then((html) => {
                const content = popup.querySelector(".popup-content");
                if (content) content.innerHTML = html;
            })
            .catch((error) => console.error("Ошибка загрузки попапа:", error));
    }

    infBlocks.forEach((infBlock, index) => {
        infBlock.addEventListener("click", () => {
            const url = `/inf${index + 1}`;
            if (popups[index]) {
                showPopup(popups[index], url);
            }
        });
    });

    closeButtons.forEach((button) => {
        button.addEventListener("click", hidePopup);
    });

    window.addEventListener("click", function (event) {
        if (!event.target.closest(".popa") && !event.target.closest('[id^="inf"]')) {
            hidePopup();
        }
    });
});

const btnShow = document.getElementById('btn_show');
const btnHide = document.getElementById('btn_hide');
const popup = document.getElementById('pop_log');

function pop_log_content (url) {

    fetch(url)
    .then((response) => response.text())
    .then((html) => {
        const content = popup.querySelector(".pop_log");
        if (content) content.innerHTML = html;
    })
    .catch((error) => console.error("Ошибка загрузки попапа:", error));
}

btnShow.addEventListener('click', function () {
    const url = '/users/login';
    pop_log_content(url);

    popup.style.display = 'block';
    console.log('PRIFFKI')
});

btnHide.addEventListener('click', function () {
    popup.style.display = 'none';
    console.log('POKA')
});
