(function () {
  if (!document.querySelector(".tag-cloud-container")) return;

  var container = document.querySelector(".tag-cloud-container");
  var width = container.clientWidth || 800;
  var height = Math.min(600, width * 0.6);

  var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);
  svg.style.display = "block";
  svg.style.margin = "0 auto";
  container.appendChild(svg);

  // Load tags from contentIndex
  fetch("/static/contentIndex.json")
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var tagMap = {};
      for (var key in data) {
        var tags = data[key].tags || [];
        for (var i = 0; i < tags.length; i++) {
          var t = tags[i];
          tagMap[t] = (tagMap[t] || 0) + 1;
        }
      }

      var entries = Object.keys(tagMap).map(function (k) {
        return { name: k, value: tagMap[k] };
      });
      entries.sort(function (a, b) { return b.value - a.value; });

      if (entries.length === 0) return;

      // Color palette matching the 7 rainbow colors
      var colors = [
        "#e74c3c", "#3498db", "#27ae60", "#f39c12",
        "#9b59b6", "#1abc9c", "#e84393"
      ];

      // D3 circle packing
      var root = d3.hierarchy({ children: entries }).sum(function (d) { return d.value; });
      var pack = d3.pack().size([width - 40, height - 40]).padding(8);
      var nodes = pack(root).leaves();

      var g = d3.select(svg);

      function getColor(i) { return colors[i % colors.length]; }

      var bubbles = g.selectAll("g").data(nodes).enter().append("g")
        .attr("class", "tag-bubble")
        .attr("transform", function (d) { return "translate(" + (d.x + 20) + "," + (d.y + 20) + ")"; })
        .style("cursor", "pointer");

      bubbles.append("circle")
        .attr("r", function (d) { return d.r; })
        .attr("fill", function (d, i) { return getColor(i); })
        .attr("fill-opacity", 0.15)
        .attr("stroke", function (d, i) { return getColor(i); })
        .attr("stroke-width", 2);

      bubbles.append("text")
        .text(function (d) { return d.data.name; })
        .attr("text-anchor", "middle")
        .attr("dy", "0.35em")
        .attr("font-size", function (d) { return Math.max(10, Math.min(d.r / 2.5, 20)); })
        .attr("fill", "#333")
        .attr("font-weight", "600")
        .attr("pointer-events", "none");

      // Click -> navigate to tag page
      bubbles.on("click", function (e, d) {
        window.location.href = "/tags/" + encodeURIComponent(d.data.name);
      });

      // Hover tooltip
      bubbles.append("title")
        .text(function (d) { return d.data.name + " (" + d.data.value + " 篇)"; });
    })
    .catch(function (err) {
      container.textContent = "标签加载失败";
      console.error(err);
    });
})();
