
const btn = document.getElementById('icon');
const menu = document.getElementById('menu');

btn.addEventListener('click', handleClick);
menu.addEventListener('click', actionMenu)

function handleClick(){
    menu.classList.toggle('show');
}

function actionMenu(event){
    console.log(event.target);
    if (event.target.classList.contains('item-menu')) {
        menu.classList.remove('show');
    }
}

