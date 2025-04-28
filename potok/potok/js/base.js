const btnShow = document.getElementById('btn_show');
const btnHide = document.getElementById('btn_hide');
const popup = document.getElementById('pop_log');

btnShow.addEventListener('click', function () {
    popup.style.display = 'block';
    console.log('PRIFFKI')
});

btnHide.addEventListener('click', function () {
    popup.style.display = 'none';
    console.log('POKA')
});
