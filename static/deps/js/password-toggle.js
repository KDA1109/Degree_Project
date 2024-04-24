$(document).ready(function() {
    $("#togglePassword1").click(function() {
        var passwordField = $("#id_password1");
        var fieldType = passwordField.attr("type");
        if (fieldType === "password") {
            passwordField.attr("type", "text");
        } else {
            passwordField.attr("type", "password");
        }
    });

    $("#togglePassword2").click(function() {
        var passwordField = $("#id_password2");
        var fieldType = passwordField.attr("type");
        if (fieldType === "password") {
            passwordField.attr("type", "text");
        } else {
            passwordField.attr("type", "password");
        }
    });
});
