let labels = document.querySelectorAll('.label-for-input');
let del_buttons = document.querySelectorAll('.delete-button');
let number = 1;
let add_button = document.querySelector('.add-button');
let div = document.querySelector('.div-with-p');


for(let l of labels){
    l.textContent += number;
    number += 1;
}

for(let d of del_buttons){
    d.addEventListener('click', del)
    }


add_button.addEventListener('click', function(){
    let p = document.querySelector('.p-for-form');
    let new_p = p.cloneNode(deep=true);
    div.append(new_p);
    indexing();
    set_zero()
    let del_buttons = document.querySelectorAll('.delete-button');
    for(let b of del_buttons){
        b.addEventListener('click', del);
    }});

function del(e){
    let del_buttons = document.querySelectorAll('.delete-button');
    if(del_buttons.length > 1){
        e.target.parentElement.remove()
    indexing();
    }
    else{
        window.alert('Техкарта должна содержать продукты')
    }
}

function indexing(){
    let labels_count = document.querySelectorAll('.label-for-input')
    let counter = 1
    for(let l of labels_count){
        l.textContent = `продукт ${counter}`;
        counter += 1
    }
}

function set_zero(){
    let inputs = document.querySelectorAll('.input-quantity')
    inputs[inputs.length - 1].value = '';
    let selects = document.querySelectorAll('.select-for-product')
    selects[selects.length - 1].value = '';
}