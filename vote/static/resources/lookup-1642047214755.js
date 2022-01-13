(function(window, undefined) {
  var dictionary = {
    "c8e5705e-7476-4e8c-9cbf-2c9736274e51": "First Link Meeting Schedule",
    "554444b6-37e1-4c68-895f-b8df2b62ca7e": "First Link Meeting Minutes Log",
    "4d8bf10e-a01f-4b5d-b529-96d077499041": "Join a Pod",
    "bb440292-3851-4fa4-a944-70b547514fd2": "Voter Settings Page",
    "39f265e7-0d0d-497b-a605-786d7f492e9c": "List of Delegates",
    "49a8bdf0-2ab7-4867-a97c-b8681087321f": "Bill Metrics",
    "ddd98a52-6b53-4880-a13f-ff2c197e0b61": "Pod Member Contact Page",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Voter Page User Type 0",
    "05f11ee1-65aa-4407-8a90-09c2a4c07c81": "Pod Number Housekeeping Page",
    "b479c273-535a-497c-963b-b363b0de9d3c": "Bill Page",
    "28953d6c-2a3a-4ba8-a2b5-b68b1520b93f": "Back-and-Forth",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);