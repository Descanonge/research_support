
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

**Importantly**, they are two versions of the MY global product:

1. **ESA-OC-CCI**: this processing is part of the Climate Change Initiative which aims at producing data for climate variables which can be use to track climate trends. Data produced by PML (Plymouth Marine Laboratory), succeeding to BC (Brockmann Consult)
2. **Copernicus-GlobColour**: Data produced by ACRI-ST using the "GlobColour processing", developped for the project of the same name. 

More on their differences later.

Data is available at a resolution of 4km for global and 1km for regional products.
Products contain standard datasets obtained with as much sensors as possible, and sometime alternative datasets restricted to Sentinel-3 OLCI data with higher resolution (1km or 300m), generally around coast only.

Here are the available products:

<table>
<thead>
  <tr>
    <th rowspan="3">Region</th>
    <th rowspan="3">Producer</th>
    <th colspan="4">Multi-Sensor</th>
    <th colspan="4">Sentinel-3 OLCI</th>
  </tr>
  <tr>
    <th colspan="2">NRT</th>
    <th colspan="2">MY</th>
    <th colspan="2">NRT</th>
    <th colspan="2">MY</th>
  </tr>
  <tr>
    <th>L3</th>
    <th>L4</th>
    <th>L3</th>
    <th>L4</th>
    <th>L3</th>
    <th>L4</th>
    <th>L3</th>
    <th>L4</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>GLO</td>
    <td>ACRI</td>
    <td>101</td>
    <td>102</td>
    <td>103</td>
    <td>104</td>
    <td>101</td>
    <td>102</td>
    <td>103</td>
    <td>104</td>
  </tr>
  <tr>
    <td>GLO</td>
    <td>PML</td>
    <td></td>
    <td></td>
    <td>107</td>
    <td>108</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ATL</td>
    <td>PML</td>
    <td>111</td>
    <td>112</td>
    <td>113</td>
    <td>114</td>
    <td>111</td>
    <td>112</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ATL</td>
    <td>ACRI</td>
    <td></td>
    <td>116</td>
    <td></td>
    <td>118</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>ARC</td>
    <td>CNR</td>
    <td></td>
    <td></td>
    <td>123</td>
    <td>124</td>
    <td>121</td>
    <td>122</td>
    <td>123</td>
    <td>124</td>
  </tr>
  <tr>
    <td>BAL</td>
    <td>CNR</td>
    <td></td>
    <td></td>
    <td>133</td>
    <td>134</td>
    <td>131</td>
    <td>132</td>
    <td>133</td>
    <td>134</td>
  </tr>
  <tr>
    <td>MED</td>
    <td>CNR</td>
    <td>141</td>
    <td>142</td>
    <td>143</td>
    <td>144</td>
    <td>141</td>
    <td>142</td>
    <td>143</td>
    <td>144</td>
  </tr>
  <tr>
    <td>BLK</td>
    <td>CNR</td>
    <td>151</td>
    <td>152</td>
    <td>153</td>
    <td>154</td>
    <td>151</td>
    <td>152</td>
    <td>153</td>
    <td>154</td>
  </tr>
</tbody>
</table>

That should help you get around on the CMEMS.
All these informations and more details (especially on the variables available in different datasets) can be found in the GlobColour user manual (the one on CMEMS): https://catalogue.marine.copernicus.eu/documents/PUM/CMEMS-OC-PUM.pdf

## Differences OC-CCI / Copernicus-GlobColour

Both products use different processing to get the same data.
Maybe most notably, in Copernicus-GlobColour the Chl is computed for each sensor *then* merge the Chl of all sensor. On the contrary, in OC-CCI the reflectances are merged across sensors and *then* the Chl is computed.
You can find some details in this paper: [Garnesson et al. 2019](https://doi.org/10.5194/os-15-819-2019). 

Both products are multi-year re-analyses, and should be appropriate to study long-term trends, however it is the explicit goal of the OC-CCI version. The [documentation](https://climate.esa.int/en/projects/ocean-colour/key-documents/) on the CCI website goes into more details on how they verify the Chl variable as a valid CDR (climate data record).

## The "GlobColour-ACRI" product

For some reason, the ACRI-ST ftp website distributes some ocean color products. It is maybe some kind of leftovers from before "standardisation" by the OCTAS-CMEMS.
You can find information about them here: https://globcolour.info/CDR_Docs/GlobCOLOUR_PUG.pdf and there: https://hermes.acri.fr

I guess I would not recommend it unless you have a reason for it.

Note that they distribute two versions: AVW (weighted average) where the Chl of all sensors are merged, and GSM (Garver, Siegel, Maritorena model) where the merge the reflectance before computing the Chl.
Some people are more familiar with those acronym.
