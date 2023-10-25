from decouple import config


# gaia_filepath = config('gaia_path')
# kepler_filepath = config('kepler_path')
near_star_filepath = config('near_star_path')
your_star_ra = float(config('your_star_ra'))
your_star_dec = float(config('your_star_dec'))
your_star_parallax = float(config('your_star_parallax'))
your_star_pmra = float(config('your_star_pmra'))
your_star_pmdec = float(config('your_star_pmdec'))
your_star_t = int(config('your_star_t'))
your_star_source_id = int(config('your_star_source_id'))
