function switchToggle_changeBgColor(toggle_id) {
    var toggle = document.querySelector("#" + toggle_id);
    toggle.classList.toggle("bg-switchToggle-brand");
}

function sidebarButtons_animation(icon_id) {
    var icon = document.querySelector("#" + icon_id);

    if (icon.style.transform == "rotateX(180deg)")
        icon.style.transform = "rotateX(0deg)";
    else
        icon.style.transform = "rotateX(180deg)";
}


// for confirm user in login in header
const btn_register = document.querySelector("#btn-confirm-login-user");
const email_form_register_login = document.querySelector("#email-form-register-login");

btn_register.addEventListener('click',()=>{
    if(email_form_register_login.value.length == 0)
    {
        email_form_register_login.style.border = "1px solid red";
        email_form_register_login.placeholder = "پر کردن این فیلد الزامی است ";
    }
    else
    {
        email_form_register_login.style.border = "1px solid #eee";
    }
})
// for confirm user in login in header
