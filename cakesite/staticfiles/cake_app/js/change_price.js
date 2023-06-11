changes = document.querySelectorAll('.hidden-button')
deletes = document.querySelectorAll('.delete-product')


for(let c of changes){
    c.addEventListener('click', change);
}
for(let d of deletes){
    d.addEventListener('click', del);
}


function change(e){
    let div = e.target.parentElement.nextElementSibling
    let divs = document.querySelectorAll('.hidden-div')
    if (div.hidden == true){
        for(let d of divs){
            d.hidden = true;
        }
        for(let c of changes){
            c.textContent = 'Изменить'
        }
        div.hidden = false;
        e.target.textContent = 'Скрыть'
    }
    else{
        div.hidden = true;
        e.target.textContent = 'Изменить'
    }}

function del(e){
    value = e.target.parentElement.parentElement.previousElementSibling.firstElementChild.textContent.split('-')[0].trim()
    result = window.confirm(`Уверены что хотите удалить продукт: "${value}?"`)
    if(result){
        input = e.target.previousElementSibling.previousElementSibling;
        input.value = ''
        input.removeAttribute('required');
        window.alert(`Продукт: "${value}" был удален`)
        }
    else{
        window.alert(`Продукт: "${value}" не был удален`)
        e.preventDefault()
    }
}