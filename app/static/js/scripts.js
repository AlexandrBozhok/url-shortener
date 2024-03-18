function copyUrl() {
    var copyText = document.getElementById("short_url");
    copyText.select();
    document.execCommand("copy");
    
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied: " + copyText.value;
  }
