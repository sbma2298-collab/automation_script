// MAXIMO SCRIPT REST ENDPOINT
//
// Example:
// /maximo/oslc/script/MXD_COUNTWOSR?site=BEDFORD

load("nashorn:mozilla_compat.js");

importPackage(Packages.psdi.server);

var woset = null;

try {
    var site = request.getQueryParam("site");

    if (site === null || String(site).trim() === "") {
        response.setStatus(400);
        response.setContentType("application/json");
        response.setContent(JSON.stringify({
            error: "The site query parameter is required."
        }));
    } else {
        site = String(site).trim().toUpperCase();

        woset = MXServer
            .getMXServer()
            .getMboSet(
                "WORKORDER",
                request.getUserInfo()
            );

        woset.setQbe(
            "SITEID",
            "=" + site
        );

        var workOrderCount = woset.count();

        response.setStatus(200);
        response.setContentType("application/json");
        response.setContent(JSON.stringify({
            site: site,
            workOrderCount: workOrderCount
        }));
    }
} catch (error) {
    response.setStatus(500);
    response.setContentType("application/json");
    response.setContent(JSON.stringify({
        error: "Unable to count work orders."
    }));

    service.log(
        "MXD_COUNTWOSR error: " + String(error)
    );
} finally {
    if (woset !== null) {
        woset.cleanup();
        woset.close();
    }
}
