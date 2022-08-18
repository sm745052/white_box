import rasterio
src = rasterio.open(input("Enter Path"))
out = input("Enter output file name")

#im2_reproj, im2_reproj_trans = reproject(
#    source=rasterio.band(im2, [1, 2, 3]),
#    dst_crs=im1.profile["crs"],
#    dst_resolution=(30, 30),
#)



#def create_dataset(data, crs, transform):
#    memfile = MemoryFile()
#    dataset = memfile.open(
#        driver="GTiff",
#        height=data.shape[1],
#        width=data.shape[2],
#        count=3,
#        crs=crs,
#        transform=transform,
#        dtype=data.dtype,
#    )
#    dataset.write(data, [1, 2, 3])
#    return dataset


#im2_reproj_ds = create_dataset(im2_reproj, im1.profile["crs"], im2_reproj_trans)

with rasterio.Env():

    # Write an array as a raster band to a new 8-bit file. For
    # the new file's profile, we start with the profile of the source
    profile = src.profile

    # And then change the band count to 1, set the
    # dtype to uint8, and specify LZW compression.
    profile.update(
        dtype=rasterio.uint8,
        count=3,
        compress='lzw')

    with rasterio.open(out, 'w', **profile) as dst:
        dst.write(src.read().astype(rasterio.uint8))
