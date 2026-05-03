const showPass = document.querySelector("#showPass")
const paswBox = document.querySelector("#password")

showPass.addEventListener(() => {
    const inputType = showPass.type === "password";
    showPass.type = inputType ? "text" : "password";
})