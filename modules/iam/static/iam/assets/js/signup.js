"use strict";

// Class definition
var KTSignupGeneral = function() {
    // Elements
    var form;
    var submitButton;
    var validator;
    var passwordMeter;

    // Handle form
    var handleForm  = function(e) {
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validator = FormValidation.formValidation(
			form,
			{
				fields: {
					'first_name': {
						validators: {
							notEmpty: {
								message: gettext('First Name is required')
							}
						}
                    },
                    'last_name': {
						validators: {
							notEmpty: {
								message: gettext('Last Name is required')
							}
						}
					},
					'email': {
                        validators: {
                            regexp: {
                                regexp: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                message: gettext('The value is not a valid email address'),
                            },
							notEmpty: {
								message: gettext('Email address is required')
							}
						}
					},
                    'password1': {
                        validators: {
                            notEmpty: {
                                message: gettext('The password is required')
                            },
                            callback: {
                                message: gettext('Please enter valid password'),
                                callback: function(input) {
                                    if (input.value.length > 0) {
                                        return validatePassword();
                                    }
                                }
                            }
                        }
                    },
				},
				plugins: {
					trigger: new FormValidation.plugins.Trigger({
                        event: {
                            password: false
                        }
                    }),
					bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: '.fv-row',
                        eleInvalidClass: '',  // comment to enable invalid state icons
                        eleValidClass: '' // comment to enable valid state icons
                    })
				}
			}
		);

        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            e.preventDefault();

            validator.revalidateField('password1');

            validator.validate().then(function(status) {
		        if (status == 'Valid') {
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
                            first_name: document.querySelector('[name="first_name"]').value,
                            last_name: document.querySelector('[name="last_name"]').value,
                            email: document.querySelector('[name="email"]').value,
                            password1: document.querySelector('[name="password1"]').value,
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
                                title: gettext('Signup Error!'),
                                text: data.message.email,
                                icon: "error",
                                buttonsStyling: false,
                                confirmButtonText: gettext("Ok, got it!"),
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            })
                            .then(function (result) {
                                if (result.isConfirmed) {
                                    form.querySelector('[name="first_name"]').value= "";
                                    form.querySelector('[name="last_name"]').value= "";
                                    form.querySelector('[name="email"]').value= "";
                                    form.querySelector('[name="password1"]').value= "";
                                }
                            });
                        }
                        else{
                            Swal.fire({
                                title: gettext('Signup Completed!'),
                                text: data.message,
                                icon: "success",
                                buttonsStyling: false,
                                confirmButtonText: gettext("Ok, got it!"),
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            }).then(function (result) {
                                if (result.isConfirmed) {

                                    form.querySelector('[name="first_name"]').value= "";
                                    form.querySelector('[name="last_name"]').value= "";
                                    form.querySelector('[name="email"]').value= "";
                                    form.querySelector('[name="password1"]').value= "";

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

                    // }).catch(function(error) {
                    //     // Show error message
                    //     console.log("entro al catch en error 400");
                    //     console.log(error);
                    //     submitButton.setAttribute('data-kt-indicator', 'off');
                    //     submitButton.disabled = false;
                    //     // Swal.fire({
                    //     //     text: error,
                    //     //     icon: "error",
                    //     //     buttonsStyling: false,
                    //     //     confirmButtonText: gettext("Ok, got it!"),
                    //     //     customClass: {
                    //     //         confirmButton: "btn btn-primary"
                    //     //     }
                    //     // });
                    // });
                }
                else {
                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                    Swal.fire({
                        text: gettext("Sorry, looks like there are some errors detected, please try again."),
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: gettext("Ok, got it!"),
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                }
		    });
        });

        // Handle password input
        form.querySelector('input[name="password1"]').addEventListener('input', function() {
            if (this.value.length > 0) {
                validator.updateFieldStatus('password1', 'NotValidated');
            }
        });
    }

    // Password input validation
    var validatePassword = function() {
        return (passwordMeter.getScore() === 100);
    }

    // Public functions
    return {
        // Initialization
        init: function() {
            // Elements
            form = document.querySelector('#kt_sign_up_form');
            submitButton = document.querySelector('#kt_sign_up_submit');
            passwordMeter = KTPasswordMeter.getInstance(form.querySelector('[data-kt-password-meter="true"]'));

            handleForm ();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTSignupGeneral.init();
});
