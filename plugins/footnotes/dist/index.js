import { visit } from "unist-util-visit";

const plugin = (userOpts) => {
  return {
    name: "Footnotes",
    htmlPlugins() {
      return [
        () => {
          return (tree) => {
            visit(tree, "element", (node) => {
              // Rename sr-only footnotes heading to visible Chinese heading
              if (
                node.tagName === "h2" &&
                node.properties?.className?.includes("sr-only") &&
                node.properties?.id === "footnote-label"
              ) {
                // Remove sr-only class
                node.properties.className = node.properties.className.filter(
                  (c) => c !== "sr-only"
                );
                if (node.properties.className.length === 0) {
                  delete node.properties.className;
                }
                // Change id
                node.properties.id = "参考资料与注释";
                // Replace text content
                if (node.children?.[0]?.value === "Footnotes") {
                  node.children[0].value = "参考资料与注释";
                }
              }

              // Add data-no-popover to footnote links
              if (
                node.tagName === "a" &&
                (node.properties?.["data-footnote-ref"] !== undefined ||
                 node.properties?.["data-footnote-backref"] !== undefined ||
                 node.properties?.href?.startsWith("#user-content-fn-"))
              ) {
                node.properties["data-no-popover"] = "true";
              }
            });
          };
        },
      ];
    },
  };
};

export default plugin;
export { plugin };
