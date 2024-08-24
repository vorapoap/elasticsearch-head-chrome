chrome.action.onClicked.addListener(function (tab) {
  chrome.tabs.create({'url': chrome.runtime.getURL('elasticsearch-head/index.html')}, function (tab) {
  });
});
