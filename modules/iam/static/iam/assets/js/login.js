"use strict";

// Class definition
var KTSigninGeneral = function() {
    // Elements
    var form;
    var submitButton;
    var validator;

    // Handle form
    var handleForm = function(e) {
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validator = FormValidation.formValidation(
			form,
			{
				fields: {					
					'login': {
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
                    'password': {
                        validators: {
                            notEmpty: {
                                message: gettext('The password is required')
                            }
                        }
                    } 
				},
				plugins: {
					trigger: new FormValidation.plugins.Trigger(),
					bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: '.fv-row',
                        eleInvalidClass: '',  // comment to enable invalid state icons
                        eleValidClass: '' // comment to enable valid state icons
                    }),
                    // icon: new FormValidation.plugins.Icon({
                    //     valid: 'fa fa-check',
                    //     invalid: 'fa fa-times',
                    //     validating: 'fa fa-refresh',
                    // }),
                    // submitButton: new FormValidation.plugins.SubmitButton(),
                    fieldStatus: new FormValidation.plugins.FieldStatus({
                        onStatusChanged: function(areFieldsValid) {
                            areFieldsValid
                                // Enable the submit button
                                // so user has a chance to submit the form again
                                ? submitButton.removeAttribute('disabled')
                                // Disable the submit button
                                : submitButton.setAttribute('disabled', 'disabled');
                        }
                    }),
				}
			}
		);

        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            // Prevent button default action
            e.preventDefault();

            // Validate form
            validator.validate().then(function (status) {
                if (status == 'Valid') {

                    // Show loading indication
                    submitButton.setAttribute('data-kt-indicator', 'on');

                    // Disable button to avoid multiple click 
                    submitButton.disabled = true;

                    // form.submit(); // submit form

                    // Interact with the API endpoint
                    messaging.getToken({vapidKey: vapid_public_key}).then((currentToken) => {
                        if (currentToken) {
                            console.log(currentToken);

                            /*var action = ["auth", "login", "create"];
                            var params = {
                                email: document.querySelector('[name="login"]').value,
                                password: document.querySelector('[name="password"]').value,
                                registration_id: currentToken,
                                device_type: "web",
                            };
                            client.action(schema, action, params).then(function(result) {
                                // Return value is in 'result'
                                // Hide loading indication
                                submitButton.removeAttribute('data-kt-indicator');
                                // Enable button
                                submitButton.disabled = false;

                                // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                                Swal.fire({
                                    text: gettext("You have successfully logged in!"),
                                    icon: "success",
                                    buttonsStyling: false,
                                    confirmButtonText: gettext("Ok, got it!"),
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                }).then(function (result) {
                                    if (result.isConfirmed) {
                                        form.querySelector('[name="login"]').value= "";
                                        form.querySelector('[name="password"]').value= "";

                                        // form.submit(); // submit form
                                        var next = document.getElementById('login_redirect_url');
                                        if (next !== null) {
                                            window.location.href = next.value;
                                        }
                                        else{
                                            window.location.href = "/";
                                        }
                                    }
                                });

                            })
                            .catch(function (error) {
                                Swal.fire({
                                    title: error,
                                    text: gettext("Sorry, an error occurred while logging in. Please try again later."),
                                    icon: "error",
                                    buttonsStyling: false,
                                    confirmButtonText: gettext("Ok"),
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                }).then(function (result) {
                                    // Hide loading indication
                                    submitButton.removeAttribute('data-kt-indicator');
                                    // Enable button
                                    submitButton.disabled = false;
                                });
                            });*/

                            fetch(form.getAttribute('action'), {
                                method: 'POST',
                                headers: {
                                  'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({
                                    email: document.querySelector('[name="login"]').value,
                                    password: document.querySelector('[name="password"]').value,
                                    registration_id: currentToken,
                                    device_type: "web",
                                })
                            }).then(function(response) {
                                if (response.ok) {
                                    // Return value is in 'result'
                                    // Hide loading indication
                                    submitButton.removeAttribute('data-kt-indicator');
                                    // Enable button
                                    submitButton.disabled = false;

                                    // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                                    Swal.fire({
                                        text: gettext("You have successfully logged in!"),
                                        icon: "success",
                                        buttonsStyling: false,
                                        confirmButtonText: gettext("Ok, got it!"),
                                        customClass: {
                                            confirmButton: "btn btn-primary"
                                        }
                                    }).then(function (result) {
                                        if (result.isConfirmed) {
                                            form.querySelector('[name="login"]').value= "";
                                            form.querySelector('[name="password"]').value= "";

                                            // form.submit(); // submit form
                                            var next = document.getElementById('login_redirect_url');
                                            if (next !== null) {
                                                window.location.href = next.value;
                                            }
                                            else{
                                                window.location.href = "/";
                                            }
                                        }
                                    });
                                } else {
                                    throw new Error('Sorry, an error occurred while signin.');
                                }
                            }).catch(function(error) {
                                Swal.fire({
                                    text: gettext("Sorry, an error occurred while signin. Please try again later."),
                                    icon: "error",
                                    buttonsStyling: false,
                                    confirmButtonText: gettext("Ok"),
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                }).then(function (result) {
                                    // Hide loading indication
                                    submitButton.removeAttribute('data-kt-indicator');
                                    // Enable button
                                    submitButton.disabled = false;
                                });
                            });


                        }
                        else {
                            // Show permission request.
                            console.log('No registration token available. Request permission to generate one.');
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
                    }).catch((err) => {
                        console.log('An error occurred while retrieving token. ', err);
                        Swal.fire({
                            text: gettext("Sorry, an error occurred while retrieving token.", err),
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: gettext("Ok, got it!"),
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        });
                    });

                } else {
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
    }

    // Public functions
    return {
        // Initialization
        init: function() {
            form = document.querySelector('#kt_sign_in_form');
            submitButton = document.querySelector('#kt_sign_in_submit');
            // submitButton = document.querySelector('#otpSubmit');

            handleForm();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTSigninGeneral.init();
});
