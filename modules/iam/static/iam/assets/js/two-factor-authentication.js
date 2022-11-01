"use strict";

var KTModalTwoFactorAuthentication = function() {
    var e, t, options, sel_opt, sms_opt, sms_form, sms_bs, sms_bc, form_mobile_validation, otp_code, otp_form, otp_bs, opt_bc, form_otp_validation, p = function() {
        options.classList.remove("d-none"), sms_opt.classList.add("d-none"), otp_code.classList.add("d-none");
    };
    return {
        init: function() {
            (e = document.querySelector("#kt_modal_two_factor_authentication")) && (t = new bootstrap.Modal(e),
            options = e.querySelector('[data-kt-element="options"]'), sel_opt = e.querySelector('[data-kt-element="options-select"]'),
            sms_opt = e.querySelector('[data-kt-element="sms"]'), sms_form = e.querySelector('[data-kt-element="sms-form"]'),
            sms_bs = e.querySelector('[data-kt-element="sms-submit"]'), sms_bc = e.querySelector('[data-kt-element="sms-cancel"]'),
            otp_code = e.querySelector('[data-kt-element="otp"]'), otp_form = e.querySelector('[data-kt-element="otp-form"]'),
            otp_bs = e.querySelector('[data-kt-element="otp-submit"]'), opt_bc = e.querySelector('[data-kt-element="otp-cancel"]'),
            sel_opt.addEventListener("click", function(e) {
                e.preventDefault();
                var t = options.querySelector('[name="auth_option"]:checked');
                options.classList.add("d-none"), "sms" == t.value ? sms_opt.classList.remove("d-none") : otp_code.classList.remove("d-none");
            }), form_mobile_validation = FormValidation.formValidation(sms_form, {
                fields: {
                    mobile: {
                        validators: {
                            notEmpty: {
                                message: "Mobile number is required"
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            }), sms_bs.addEventListener("click", function(e) {
                e.preventDefault(),
                form_mobile_validation && form_mobile_validation.validate().then(function(e) {
                    console.log("validated!"), "Valid" == e ? (sms_bs.setAttribute("data-kt-indicator", "on"),
                    sms_bs.disabled = !0,
                        setTimeout(function() {

                        sms_opt.classList.add("d-none");
                        otp_code.classList.remove("d-none");

                        /*sms_bs.removeAttribute("data-kt-indicator"), sms_bs.disabled = !1, Swal.fire({
                            text: "Mobile number has been successfully submitted!",
                            icon: "success",
                            buttonsStyling: !1,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        }).then(function(e) {
                            e.isConfirmed && (t.hide(), p());
                        });*/
                    }, 2e3)) : Swal.fire({
                        text: "Sorry, looks like there are some errors detected, please try again.",
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                });
            }), sms_bc.addEventListener("click", function(e) {
                e.preventDefault(), options.querySelector('[name="auth_option"]:checked'), options.classList.remove("d-none"),
                sms_opt.classList.add("d-none");
            }), form_otp_validation = FormValidation.formValidation(otp_form, {
                fields: {
                    code: {
                        validators: {
                            notEmpty: {
                                message: "Code is required"
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            }), otp_bs.addEventListener("click", function(e) {
                e.preventDefault(), form_otp_validation && form_otp_validation.validate().then(function(e) {
                    console.log("validated!"), "Valid" == e ? (otp_bs.setAttribute("data-kt-indicator", "on"),
                    otp_bs.disabled = !0, setTimeout(function() {
                        otp_bs.removeAttribute("data-kt-indicator"), otp_bs.disabled = !1, Swal.fire({
                            text: "Code has been successfully submitted!",
                            icon: "success",
                            buttonsStyling: !1,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        }).then(function(e) {
                            e.isConfirmed && (t.hide(), p());
                        });
                    }, 2e3)) : Swal.fire({
                        text: "Sorry, looks like there are some errors detected, please try again.",
                        icon: "error",
                        buttonsStyling: !1,
                        confirmButtonText: "Ok, got it!",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                });
            }), opt_bc.addEventListener("click", function(e) {
                e.preventDefault(), options.querySelector('[name="auth_option"]:checked'), options.classList.remove("d-none"),
                otp_code.classList.add("d-none");
            }));
        }
    };
}();

KTUtil.onDOMContentLoaded(function() {
    KTModalTwoFactorAuthentication.init();
});