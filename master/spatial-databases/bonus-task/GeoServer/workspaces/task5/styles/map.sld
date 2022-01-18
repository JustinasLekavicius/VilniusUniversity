<?xml version="1.0" encoding="utf8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd">
  <NamedLayer>
    <Name>map</Name>
    <UserStyle>
      <Title>map</Title>
      <FeatureTypeStyle>
        <Rule>
          <Name>map, Z=0</Name>
          <RasterSymbolizer>
            <Opacity>1.0</Opacity>
            <ChannelSelection>
              <RedChannel>
                <SourceChannelName>1</SourceChannelName>
              </RedChannel>
              <GreenChannel>
                <SourceChannelName>2</SourceChannelName>
              </GreenChannel>
              <BlueChannel>
                <SourceChannelName>3</SourceChannelName>
              </BlueChannel>
            </ChannelSelection>
          </RasterSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
