let btn = document.querySelector('.clear-button');
let input_product_name = document.querySelector('.form-input-product-name');
let input_product_price = document.querySelector('.form-input-product-price');
let input_cake_name = document.querySelector('.form-input-cake-name');
let input_cake_description = document.querySelector('.form-input-cake-description');
let input_cake_slug = document.querySelector('.form-input-cake-slug');
let input_cake_photo = document.querySelector('.form-input-cake-photo');

console.log(input_product_name)
console.log(input_product_price)
console.log(input_cake_name)
console.log(input_cake_description)
console.log(input_cake_slug)
console.log(input_cake_photo)




btn.addEventListener('click', function() {
    if(input_product_name){
        input_product_name.value = '';
    }
    if(input_product_price){
        input_product_price.value = '';
    }
    if(input_cake_name){
        input_cake_name.value = '';
    }
    if(input_cake_description){
        input_cake_description.value = '';
    }
    if(input_cake_slug){
        input_cake_slug.value = '';
    }
    if(input_cake_photo){
        input_cake_photo.value = '';
    }
    });