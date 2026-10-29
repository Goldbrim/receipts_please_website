export default function (eleventyConfig) {
  // Files copied to the site as-is.
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/styles.css");
  eleventyConfig.addPassthroughCopy("src/CNAME");
  eleventyConfig.addPassthroughCopy({ "src/assets/apple-touch-icon.png": "apple-touch-icon.png" });
  eleventyConfig.addPassthroughCopy({ "src/assets/favicon.ico": "favicon.ico" });

  // Absolute URL for canonical links, Open Graph tags and the sitemap.
  eleventyConfig.addFilter("absoluteUrl", (path, base) => new URL(path, base).href);

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    templateFormats: ["njk"],
    htmlTemplateEngine: "njk",
  };
}
