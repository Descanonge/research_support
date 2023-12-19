# Ocean Colour

This mini-guide stems from encountering some confusion when discussing with collaborators about which kind of Chlorophyll (Chl) data we were using. 
To avoid future headaches, here is a small overview of the current state of distributed ocean colour data, mainly Chl.

## Chlorophyll-a from ocean colour ?

If needed, a very quick primer on how Chl is obtained from satellite data.
The concept is simple enough: Chlorophyll absorbs blue and red wavelength, which makes the ocean appear greener.
Following this, we can filter out atmospheric interferences to get "reflectances", and relate the Chl concentration to a ratio of reflectances at different wavelengths.

There are different algorithm using more bands, in more complex ways. Some are more adapted to regions of high concentration of Chl. To add to this complexity, different satellite have different bands (wavelengths), which must be accounted for of course.

More details at https://oceancolour.gsfc.nasa.gov/resources/, in particular https://www.earthdata.nasa.gov/apt/documents/chlor-a/v1.0. 

## Different products

As of december 2023, it appears the main available ocean colour / Chl products are those part of OCTAC (Ocean Colour Thematic Assembly Center), and are distributed by the [CMEMS/Copernicus](https://data.marine.copernicus.eu/products).

There are two kind of products: **NRT** (near real time), the data is available quickly (within 24 hours typically) but the processing is less involved; and **MY** (multi-year) which is updated every few years by reprocessing the whole time series.
NRT is useful for case studies, in-situ campaign, but otherwise the MY reprocessing is advised.

They are different products for different regions: **GLO** (Global), **ACR** (Arctic Ocean), **BAL** (Baltic Sea), **ATL** (Atlantic Ocean), **MED** (Mediterranean Sea), **BLK** (Black Sea).

They are available at two levels of processing: **L3** and **L4** which is an interpolated version of L3 that removes clouds / invalid pixels.

**Importantly**, they are two versions of the MY global product.

1. ESA-OC-CCI: this processing is part of the Climate Change Initiative which aims at producing data for climate variables which can be use to track climate trends. Data produced by PML (Plymouth Marine Laboratory), succeeding to BC (Brockmann Consult)
2. Copernicus-GlobColour: Data produced by ACRI-ST using the "GlobColour processing", developped for the project of the same name. 

More on their differences later.

Each combinaison of the parameters listed has a code:

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;}
.tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ztna{background-color:#409cff;border-color:#ffffff;color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-ru5h{background-color:#409cff;border-color:#ffffff;color:#ffffff;text-align:center;vertical-align:top}
.tg .tg-9zno{background-color:#ebf5ff;border-color:#9abad9;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-6gz9{background-color:#ebf5ff;border-color:#9abad9;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-ztna" rowspan="3">Region</th>
    <th class="tg-ztna" rowspan="3">Producer</th>
    <th class="tg-ztna" colspan="4">Multi-Sensor</th>
    <th class="tg-ztna" colspan="4">Sentinel-3 OLCI</th>
  </tr>
  <tr>
    <th class="tg-ru5h" colspan="2">NRT</th>
    <th class="tg-ru5h" colspan="2">MY</th>
    <th class="tg-ru5h" colspan="2">NRT</th>
    <th class="tg-ru5h" colspan="2">MY</th>
  </tr>
  <tr>
    <th class="tg-ru5h">L3</th>
    <th class="tg-ru5h">L4</th>
    <th class="tg-ru5h">L3</th>
    <th class="tg-ru5h">L4</th>
    <th class="tg-ru5h">L3</th>
    <th class="tg-ru5h">L4</th>
    <th class="tg-ru5h">L3</th>
    <th class="tg-ru5h">L4</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9zno">GLO</td>
    <td class="tg-9zno">ACRI</td>
    <td class="tg-6gz9">101</td>
    <td class="tg-6gz9">102</td>
    <td class="tg-6gz9">103</td>
    <td class="tg-6gz9">104</td>
    <td class="tg-6gz9">101</td>
    <td class="tg-6gz9">102</td>
    <td class="tg-6gz9">103</td>
    <td class="tg-6gz9">104</td>
  </tr>
  <tr>
    <td class="tg-9zno">GLO</td>
    <td class="tg-9zno">PML</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9">107</td>
    <td class="tg-6gz9">108</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
  </tr>
  <tr>
    <td class="tg-9zno">ATL</td>
    <td class="tg-9zno">PML</td>
    <td class="tg-6gz9">111</td>
    <td class="tg-6gz9">112</td>
    <td class="tg-6gz9">113</td>
    <td class="tg-6gz9">114</td>
    <td class="tg-6gz9">111</td>
    <td class="tg-6gz9">112</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
  </tr>
  <tr>
    <td class="tg-9zno">ATL</td>
    <td class="tg-9zno">ACRI</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9">116</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9">118</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
  </tr>
  <tr>
    <td class="tg-9zno">ARC</td>
    <td class="tg-9zno">CNR</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9">123</td>
    <td class="tg-6gz9">124</td>
    <td class="tg-6gz9">121</td>
    <td class="tg-6gz9">122</td>
    <td class="tg-6gz9">123</td>
    <td class="tg-6gz9">124</td>
  </tr>
  <tr>
    <td class="tg-9zno">BAL</td>
    <td class="tg-9zno">CNR</td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9"></td>
    <td class="tg-6gz9">133</td>
    <td class="tg-6gz9">134</td>
    <td class="tg-6gz9">131</td>
    <td class="tg-6gz9">132</td>
    <td class="tg-6gz9">133</td>
    <td class="tg-6gz9">134</td>
  </tr>
  <tr>
    <td class="tg-9zno">MED</td>
    <td class="tg-9zno">CNR</td>
    <td class="tg-6gz9">141</td>
    <td class="tg-6gz9">142</td>
    <td class="tg-6gz9">143</td>
    <td class="tg-6gz9">144</td>
    <td class="tg-6gz9">141</td>
    <td class="tg-6gz9">142</td>
    <td class="tg-6gz9">143</td>
    <td class="tg-6gz9">144</td>
  </tr>
  <tr>
    <td class="tg-9zno">BLK</td>
    <td class="tg-9zno">CNR</td>
    <td class="tg-6gz9">151</td>
    <td class="tg-6gz9">152</td>
    <td class="tg-6gz9">153</td>
    <td class="tg-6gz9">154</td>
    <td class="tg-6gz9">151</td>
    <td class="tg-6gz9">152</td>
    <td class="tg-6gz9">153</td>
    <td class="tg-6gz9">154</td>
  </tr>
</tbody>
</table>

That should help you get around on the CMEMS.
All these informations (and more details) can be found in the GlobColour user manual (the one on CMEMS): https://catalogue.marine.copernicus.eu/documents/PUM/CMEMS-OC-PUM.pdf

## The GlobColour-ACRI product

## Differences OC-CCI / Copernicus-GlobColour
