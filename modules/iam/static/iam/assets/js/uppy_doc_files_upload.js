"use strict";

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Class definition
var KTUppy = (function() {
  const Uppy = window.Uppy;
  const Tus = Uppy.Tus;
  const ProgressBar = Uppy.ProgressBar;
  const StatusBar = Uppy.StatusBar;
  const FileInput = Uppy.FileInput;
  const Informer = Uppy.Informer;
  const XHRUpload = Uppy.XHRUpload;

  // to get uppy companions working, please refer to the official documentation here: https://uppy.io/docs/companion/
  const Dashboard = Uppy.Dashboard;
  const Webcam = Uppy.Webcam;

  var api_documents_endpoint = document.currentScript.dataset.url;

  var initMediaFileUploads = function() {
    var id = "#kt_uppy_mediafiles_upload";
    var options = {
      proudlyDisplayPoweredByUppy: false,
      target: id + " .kt-uppy__dashboard",
      inline: false,
      replaceTargetContent: true,
      showProgressDetails: true,
      hideUploadButton: false,
      // note: "No filetype restrictions.",
      height: 470,
      // metaFields: [
      //   { id: "name", name: "name", placeholder: "File name" }
      // ],
      browserBackButtonClose: true,
      locale: {
        strings: {
          selectToUpload: gettext('Select o capture your documents'),
          browse: gettext('browse'),
        }
      },
      trigger: id + " .kt-uppy__btn"
    };

    var uppy_lang = window.Uppy.locales.en_US;
    if (window.user_lang === "es"){
        uppy_lang = window.Uppy.locales.es_ES;
    }

    var uppyDashboard = Uppy.Core({
      // autoProceed: true,
      locale: uppy_lang,
      restrictions: {
        maxFileSize: 10485760, // 10mb
        maxNumberOfFiles: 10,
        minNumberOfFiles: 1,
        allowedFileTypes: ['image/*']
        // allowedFileTypes: ['image/*', 'video/*', '.pdf', '.PDF', '.doc', '.docx', '.xls', '.xlsx']
      }
    });

    uppyDashboard.use(Dashboard, options);
    uppyDashboard.use(Webcam, { target: Dashboard });
    uppyDashboard.use(XHRUpload, {
      id: "XHRUpload",
      // endpoint: "/en/accounting/documents/"+window.doc_type+"/upload-files/",
      endpoint: api_documents_endpoint,
      method: "post",
      formData: true,
      fieldName: "files",
      bundle: "true",
      headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    uppyDashboard.on("complete", function() {
      window.location.reload();
    });
  };

  return {
    // public functions
    init: function() {
      initMediaFileUploads();
    }
  };
})();

KTUtil.onDOMContentLoaded((
    function(){
        KTUppy.init();
    }
));
