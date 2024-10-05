window.onload = function () {
    if (location.href.contains("/_plugin/")) {
        var base_uri = location.href.replace(/_plugin\/.*/, "");
    }
    var args = location.search
        .substring(1)
        .split("&")
        .reduce(function (r, p) {
            r[decodeURIComponent(p.split("=")[0])] = decodeURIComponent(p.split("=")[1]);
            return r;
        }, {});
    new app.App("body", {
        id: "es",
        base_uri: args["base_uri"] || base_uri,
        auth_user: args["auth_user"] || "",
        auth_password: args["auth_password"],
        dashboard: args["dashboard"],
    });
};
