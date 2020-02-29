browser.browserAction.onClicked.addListener(Initialize);

function OnOk(response)
{
    console.log(`Received ${response}`);
}

function OnErr()
{
    console.log(`Error: ${error}`);
    browser.tabs.create();
}

function Initialize()
{
    console.log("Initialize");

    var q = browser.tabs.query({
        currentWindow:true,
        active:true
    });
    
    q.then(OnActiveTab, OnErr);
}

function OnActiveTab(tabs)
{
    if (!tabs[0])
        return;
    
    var sent = browser.runtime.sendNativeMessage("VojtechLofflerDownloader", tabs[0].url);
    sent.then(OnOk, OnErr);
}

