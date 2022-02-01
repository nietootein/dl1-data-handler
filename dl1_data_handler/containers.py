from astropy import units as u
from ctapipe.core import Container, Field
from numpy import nan


class MAGICMCHeaderContainer(Container):
    corsika_version = Field(nan, "CORSIKA version *  1000")
    refl_version = Field(nan, "refl version")
    cam_version = Field(nan, "camera version")
    run_number = Field(nan, "MC Run Number")
    prod_site = Field(nan, "Production site")
    date_run_mmcs = Field(nan, "Date Run MMCs")
    date_run_cam = Field(nan, "Date Run Camera")
    energy_range_max = Field(nan * u.TeV, "Energy Range Maximum", unit=u.TeV)
    energy_range_min = Field(nan * u.TeV, "Energy Range Minimum", unit=u.TeV)
    max_az = Field(nan * u.rad, "Shower Azimuth Maximum", unit=u.rad)
    min_az = Field(nan * u.rad, "Shower Azimuth Minimum", unit=u.rad)
    max_alt = Field(nan * u.rad, "Shower Altitude Maximum", unit=u.rad)
    min_alt = Field(nan * u.rad, "Shower Altitude Minimum", unit=u.rad)
    c_wave_lower = Field(nan, "C Wave Lower")
    c_wave_upper = Field(nan, "C Wave Upper")
    num_obs_lev = Field(nan, "Number Observations Level")
    spectral_index = Field(nan, "Spectral Index")
    max_viewcone_radius = Field(nan * u.deg, "Viewcone Radius Maximum", unit=u.deg)
    max_scatter_range = Field(nan, "Scatter Range Maximum")
    star_field_rotate = Field(nan, "Star Field Rotate")
    star_field_ra_h = Field(nan, "Star Field RA H")
    star_field_ra_m = Field(nan, "Star Field RA M")
    star_field_ra_s = Field(nan, "Star Field RA S")
    star_field_dec_d = Field(nan, "Star Field DEC D")
    star_field_dec_m = Field(nan, "Star Field DEC M")
    star_field_dec_s = Field(nan, "Star Field DEC S")
    num_trig_cond = Field(nan, "Number Trigger Condition")
    all_evts_trig = Field(nan, "All Events Triggered")
    mc_evt = Field(nan, "MC Event")
    mc_trig = Field(nan, "MC Trigger")
    mc_fadc = Field(nan, "MC Fadc")
    raw_evt = Field(nan, "Raw Event")
    num_analised_pix = Field(nan, "Number of Analised Pixels")
    num_showers = Field(nan, "Number of Events")
    num_phe_from_dnsb = Field(nan, "Number Phe from DNSB")
    elec_noise = Field(nan, "Elec Noise")
    optic_links_noise = Field(nan, "Optic Links Noise")


class MAGICHeaderContainer(Container):
    camera_version = Field(nan, "Camera Version")
    fadc_type = Field(nan, "FADC type")
    fadc_resolution = Field(nan, "FADC resolution")
    format_version = Field(nan, "Format version")
    magic_number = Field(nan, "MAGIC number")
    num_bytes_per_sample = Field(nan, "Number of bytes per sample")
    num_crates = Field(nan, "Number of crates")
    num_pix_in_crate = Field(nan, "Number of pixels per crate")
    num_samples_hi_gain = Field(nan, "Number of High gain samples")
    num_samples_lo_gain = Field(nan, "Number of Low gain samples")
    num_samples_removed_head = Field(nan, "Number of samples removed from the head")
    num_samples_removed_tail = Field(nan, "Number of samples removed from the tail")
    run_type = Field(nan, "Run type")
    online_domino_calib = Field(nan, "Online domino calibration")
    sample_frequency = Field(nan, "Sample frequency")
    soft_version = Field(nan, "Soft version")
    source_epoch_date = Field(nan, "Source epoch date")
    num_events = Field(nan, "Number of events")
    num_events_read = Field(nan, "Number of events read")
    channel_header_size = Field(nan, "Channel header size")
    event_header_size = Field(nan, "Event header size")
    run_header_size = Field(nan, "Run header size")
    run_number = Field(nan, "Run number")
    subrun_index = Field(nan, "Subrun index")
    source_dec = Field(nan, "Source Dec")
    source_ra = Field(nan, "Source RA")
    telescope_dec = Field(nan, "Telescope Dec")
    telescope_ra = Field(nan, "Telescope RA")
    observation_mode = Field(nan, "Observation mode")
    project_name = Field(nan, "Project name")
    source_epoch_char = Field(nan, "Source epoch char")
    source_name = Field(nan, "Source name")
    calib_coeff_filename = Field(nan, "Calibration coefficient filename")
    run_start_mjd = Field(nan, "Start date MJD")
    run_start_ms = Field(nan, "Start time in ms")
    run_start_ns = Field(nan, "Start time in ns")
    run_stop_mjd = Field(nan, "Stop date MJD")
    run_stop_ms = Field(nan, "Stop time in ms")
    run_stop_ns = Field(nan, "Stop time in ns")
