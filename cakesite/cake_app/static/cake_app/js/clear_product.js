let btn = document.querySelector('.clear-button');
let input_product_name = document.querySelector('.form-input-product-name');
let input_product_price = document.querySelector('.form-input-product-price');
let input_cake_name = document.querySelector('.form-input-cake-name');
let input_cake_description = document.querySelector('.form-input-cake-description');
let input_cake_slug = document.querySelector('.form-input-cake-slug');
let input_cake_photo = document.querySelector('.form-input-cake-photo');
let input_tech_cake = document.querySelector('#id_model_cake');
let input_tech_product = document.querySelector('#id_model_product');
let input_tech_quantity = document.querySelector('.form-input-techcard-quantity');


console.log(input_product_name);
console.log(input_product_price);
console.log(input_cake_name);
console.log(input_cake_description);
console.log(input_cake_slug);
console.log(input_cake_photo);
console.log(input_tech_cake);
console.log(input_tech_product);
console.log(input_tech_quantity);





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
    if(input_tech_cake){
        input_tech_cake.value = '';
    }
    if(input_tech_product){
        input_tech_product.value = '';
    }
    if(input_tech_quantity){
        input_tech_quantity.value = '';
    }
    });