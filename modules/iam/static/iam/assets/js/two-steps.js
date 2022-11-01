"use strict";

// Class Definition
var KTSigninTwoSteps = function() {
    // Elements
    var form;
    var submitButton;
    var validation_code;

    // Handle form
    var handleForm = function(e) {        
        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            e.preventDefault();

            var validated = true;

            var inputs = [].slice.call(form.querySelectorAll('input[maxlength="1"]'));
            inputs.map(function (input) {
                if (input.value === '' || input.value.length === 0) {
                    validated = false;
                }
            });

            if (validated === true) {
                // Show loading indication
                submitButton.setAttribute('data-kt-indicator', 'on');

                // Disable button to avoid multiple click 
                submitButton.disabled = true;

                fetch(form.getAttribute('action'), {
                        method: 'POST',
                        headers: {
                          'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            user_email: user_email,
                            validation_code: validation_code,
                        })
                    })
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        console.log(data);
                        if(data.error){
                            submitButton.setAttribute('data-kt-indicator', 'off');
                            submitButton.disabled = false;

                            Swal.fire({
                                title: gettext('Account Validation Error!'),
                                text: data.message,
                                icon: "error",
                                buttonsStyling: false,
                                confirmButtonText: gettext("Ok, got it!"),
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            })
                            .then(function (result) {
                                if (result.isConfirmed) {
                                    inputs.map(function (input) {
                                        input.value = '';
                                    });
                                }
                            });
                        }
                        else{
                            Swal.fire({
                                title: gettext('Account Validation Completed!'),
                                text: data.message,
                                icon: "success",
                                buttonsStyling: false,
                                confirmButtonText: gettext("Ok, got it!"),
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            }).then(function (result) {
                                if (result.isConfirmed) {

                                    inputs.map(function (input) {
                                        input.value = '';
                                    });

                                    const redirect_url = data.next_url;
                                    const next = document.getElementById('login_redirect_url');

                                    if (redirect_url !== null){
                                        window.location.href = redirect_url;
                                    }
                                    else{
                                        if (next !== null) {
                                            window.location.href = next.value;
                                        }
                                        else{
                                            window.location.href = "/";
                                        }
                                    }


                                }
                            });
                        }

                    })
                    .catch(error => {
                        // console.log(error);
                        submitButton.setAttribute('data-kt-indicator', 'off');
                        submitButton.disabled = false;
                    });


            } else {
                swal.fire({
                    text: gettext("Please enter valid verification code and try again."),
                    icon: "error",
                    buttonsStyling: false,
                    confirmButtonText: "Ok, got it!",
                    customClass: {
                        confirmButton: "btn fw-bold btn-light-primary"
                    }
                }).then(function() {
                    KTUtil.scrollTop();
                });
            }
        });
    }

    var handleType = function() {
        var input1 = form.querySelector("[name=code_1]");
        var input2 = form.querySelector("[name=code_2]");
        var input3 = form.querySelector("[name=code_3]");
        var input4 = form.querySelector("[name=code_4]");
        var input5 = form.querySelector("[name=code_5]");
        var input6 = form.querySelector("[name=code_6]");

        input1.focus();

        input1.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input2.focus();
            }
        });

        input2.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input3.focus();
            }
        });

        input3.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input4.focus();
            }
        });

        input4.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input5.focus();
            }
        });

        input5.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input6.focus();
            }
        });
        
        input6.addEventListener("keyup", function() {
            if (this.value.length === 1) {
                input6.blur();
                validation_code = input1.value + input2.value + input3.value + input4.value + input5.value + input6.value;
            }
        });

    };

    // Public functions
    return {
        // Initialization
        init: function() {
            form = document.querySelector('#kt_sing_in_two_steps_form');
            submitButton = document.querySelector('#kt_sing_in_two_steps_submit');

            handleForm();
            handleType();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTSigninTwoSteps.init();
});