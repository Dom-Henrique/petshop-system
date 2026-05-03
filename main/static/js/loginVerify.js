// verificar se os campos estao devidamente preenchidos
let emailBox = document.querySelector('#emailBox');
let paswBox = document.querySelector("#password");
let loginBT = document.querySelector(".login-bt");
let signBT = document.querySelector(".sign_bt");

function validateFields(){
    // verificar o email
    if ((emailBox.value.includes("@") && emailBox.value.includes(".com")) && paswBox.value.length>=8){
        loginBT.disabled = false;
        signBT.disabled = false;
    }
    else {
        loginBT.disabled = true;
        signBT.disabled = true;
    }
}

emailBox.addEventListener("input", validateFields);
paswBox.addEventListener("input", validateFields)