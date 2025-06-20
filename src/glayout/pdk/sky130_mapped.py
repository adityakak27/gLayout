from src.glayout.pdk.mappedpdk import MappedPDK, SetupPDKFiles
from src.glayout import via_stack
from pathlib import Path
from src.glayout.primitives import fet
from .sky130_add_npc import sky130_add_npc


grulesobj = dict()
for glayer in MappedPDK.valid_glayers:
    grulesobj[glayer] = dict((x, None) for x in MappedPDK.valid_glayers)

grulesobj["dnwell"]["dnwell"] = {"min_width": 3.0, "min_separation": 6.3}
grulesobj["dnwell"]["pwell"] = {"min_enclosure": 0.0}
grulesobj["dnwell"]["nwell"] = {"min_separation": 4.5}
grulesobj["dnwell"]["p+s/d"] = {}
grulesobj["dnwell"]["n+s/d"] = {}
grulesobj["dnwell"]["active_diff"] = {}
grulesobj["dnwell"]["active_tap"] = {"min_separation": 0.34}
grulesobj["dnwell"]["poly"] = {}
grulesobj["dnwell"]["mcon"] = {}
grulesobj["dnwell"]["met1"] = {}
grulesobj["dnwell"]["via1"] = {}
grulesobj["dnwell"]["met2"] = {}
grulesobj["dnwell"]["via2"] = {}
grulesobj["dnwell"]["met3"] = {}
grulesobj["dnwell"]["via3"] = {}
grulesobj["dnwell"]["met4"] = {}
grulesobj["dnwell"]["via4"] = {}
grulesobj["dnwell"]["met5"] = {}
grulesobj["dnwell"]["capmet"] = {}
grulesobj["pwell"]["dnwell"] = {}
grulesobj["pwell"]["pwell"] = {}
grulesobj["pwell"]["nwell"] = {}
grulesobj["pwell"]["p+s/d"] = {}
grulesobj["pwell"]["n+s/d"] = {}
grulesobj["pwell"]["active_diff"] = {}
grulesobj["pwell"]["active_tap"] = {"min_enclosure": 0.18}
grulesobj["pwell"]["poly"] = {}
grulesobj["pwell"]["mcon"] = {}
grulesobj["pwell"]["met1"] = {}
grulesobj["pwell"]["via1"] = {}
grulesobj["pwell"]["met2"] = {}
grulesobj["pwell"]["via2"] = {}
grulesobj["pwell"]["met3"] = {}
grulesobj["pwell"]["via3"] = {}
grulesobj["pwell"]["met4"] = {}
grulesobj["pwell"]["via4"] = {}
grulesobj["pwell"]["met5"] = {}
grulesobj["pwell"]["capmet"] = {}
grulesobj["nwell"]["dnwell"] = {}
grulesobj["nwell"]["pwell"] = {}
grulesobj["nwell"]["nwell"] = {"min_width": 0.84, "min_separation": 1.27}
grulesobj["nwell"]["p+s/d"] = {}
grulesobj["nwell"]["n+s/d"] = {}
grulesobj["nwell"]["active_diff"] = {}
grulesobj["nwell"]["active_tap"] = {"min_enclosure": 0.18}
grulesobj["nwell"]["poly"] = {}
grulesobj["nwell"]["mcon"] = {}
grulesobj["nwell"]["met1"] = {}
grulesobj["nwell"]["via1"] = {}
grulesobj["nwell"]["met2"] = {}
grulesobj["nwell"]["via2"] = {}
grulesobj["nwell"]["met3"] = {}
grulesobj["nwell"]["via3"] = {}
grulesobj["nwell"]["met4"] = {}
grulesobj["nwell"]["via4"] = {}
grulesobj["nwell"]["met5"] = {}
grulesobj["nwell"]["capmet"] = {}
grulesobj["p+s/d"]["dnwell"] = {}
grulesobj["p+s/d"]["pwell"] = {}
grulesobj["p+s/d"]["nwell"] = {}
grulesobj["p+s/d"]["p+s/d"] = {"min_width": 0.38, "min_separation": 0.38}
grulesobj["p+s/d"]["n+s/d"] = {}
grulesobj["p+s/d"]["active_diff"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["p+s/d"]["active_tap"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["p+s/d"]["poly"] = {}
grulesobj["p+s/d"]["mcon"] = {}
grulesobj["p+s/d"]["met1"] = {}
grulesobj["p+s/d"]["via1"] = {}
grulesobj["p+s/d"]["met2"] = {}
grulesobj["p+s/d"]["via2"] = {}
grulesobj["p+s/d"]["met3"] = {}
grulesobj["p+s/d"]["via3"] = {}
grulesobj["p+s/d"]["met4"] = {}
grulesobj["p+s/d"]["via4"] = {}
grulesobj["p+s/d"]["met5"] = {}
grulesobj["p+s/d"]["capmet"] = {}
grulesobj["n+s/d"]["dnwell"] = {}
grulesobj["n+s/d"]["pwell"] = {}
grulesobj["n+s/d"]["nwell"] = {}
grulesobj["n+s/d"]["p+s/d"] = {}
grulesobj["n+s/d"]["n+s/d"] = {"min_width": 0.38, "min_separation": 0.38}
grulesobj["n+s/d"]["active_diff"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["n+s/d"]["active_tap"] = {"min_enclosure": 0.13, "min_separation": 0.13}
grulesobj["n+s/d"]["poly"] = {}
grulesobj["n+s/d"]["mcon"] = {}
grulesobj["n+s/d"]["met1"] = {}
grulesobj["n+s/d"]["via1"] = {}
grulesobj["n+s/d"]["met2"] = {}
grulesobj["n+s/d"]["via2"] = {}
grulesobj["n+s/d"]["met3"] = {}
grulesobj["n+s/d"]["via3"] = {}
grulesobj["n+s/d"]["met4"] = {}
grulesobj["n+s/d"]["via4"] = {}
grulesobj["n+s/d"]["met5"] = {}
grulesobj["n+s/d"]["capmet"] = {}
grulesobj["active_diff"]["dnwell"] = {}
grulesobj["active_diff"]["pwell"] = {}
grulesobj["active_diff"]["nwell"] = {}
grulesobj["active_diff"]["p+s/d"] = {}
grulesobj["active_diff"]["n+s/d"] = {}
grulesobj["active_diff"]["active_diff"] = {"min_width": 0.15, "min_separation": 0.27}
grulesobj["active_diff"]["active_tap"] = {"min_separation": 0.27}
grulesobj["active_diff"]["poly"] = {"overhang": 0.25}
grulesobj["active_diff"]["mcon"] = {"min_enclosure": 0.06}
grulesobj["active_diff"]["met1"] = {}
grulesobj["active_diff"]["via1"] = {}
grulesobj["active_diff"]["met2"] = {}
grulesobj["active_diff"]["via2"] = {}
grulesobj["active_diff"]["met3"] = {}
grulesobj["active_diff"]["via3"] = {}
grulesobj["active_diff"]["met4"] = {}
grulesobj["active_diff"]["via4"] = {}
grulesobj["active_diff"]["met5"] = {}
grulesobj["active_diff"]["capmet"] = {}
grulesobj["active_tap"]["dnwell"] = {}
grulesobj["active_tap"]["pwell"] = {}
grulesobj["active_tap"]["nwell"] = {}
grulesobj["active_tap"]["p+s/d"] = {}
grulesobj["active_tap"]["n+s/d"] = {}
grulesobj["active_tap"]["active_diff"] = {}
grulesobj["active_tap"]["active_tap"] = {"min_width": 0.15, "min_separation": 0.27}
grulesobj["active_tap"]["poly"] = {}
grulesobj["active_tap"]["mcon"] = {"min_enclosure": 0.12}
grulesobj["active_tap"]["met1"] = {}
grulesobj["active_tap"]["via1"] = {}
grulesobj["active_tap"]["met2"] = {}
grulesobj["active_tap"]["via2"] = {}
grulesobj["active_tap"]["met3"] = {}
grulesobj["active_tap"]["via3"] = {}
grulesobj["active_tap"]["met4"] = {}
grulesobj["active_tap"]["via4"] = {}
grulesobj["active_tap"]["met5"] = {}
grulesobj["active_tap"]["capmet"] = {}
grulesobj["poly"]["dnwell"] = {}
grulesobj["poly"]["pwell"] = {}
grulesobj["poly"]["nwell"] = {}
grulesobj["poly"]["p+s/d"] = {}
grulesobj["poly"]["n+s/d"] = {}
grulesobj["poly"]["active_diff"] = {}
grulesobj["poly"]["active_tap"] = {}
grulesobj["poly"]["poly"] = {
    "min_width": 0.15,
    "min_separation": 0.21,
    "extension": 0.13,
}
grulesobj["poly"]["mcon"] = {"min_enclosure": 0.05, "min_separation": 0.06}
grulesobj["poly"]["met1"] = {}
grulesobj["poly"]["via1"] = {}
grulesobj["poly"]["met2"] = {}
grulesobj["poly"]["via2"] = {}
grulesobj["poly"]["met3"] = {}
grulesobj["poly"]["via3"] = {}
grulesobj["poly"]["met4"] = {}
grulesobj["poly"]["via4"] = {}
grulesobj["poly"]["met5"] = {}
grulesobj["poly"]["capmet"] = {}
grulesobj["mcon"]["dnwell"] = {}
grulesobj["mcon"]["pwell"] = {}
grulesobj["mcon"]["nwell"] = {}
grulesobj["mcon"]["p+s/d"] = {}
grulesobj["mcon"]["n+s/d"] = {}
grulesobj["mcon"]["active_diff"] = {}
grulesobj["mcon"]["active_tap"] = {}
grulesobj["mcon"]["poly"] = {"min_enclosure": 0.08}
grulesobj["mcon"]["mcon"] = {"min_width": 0.17, "min_separation": 0.17, "width": 0.17}
grulesobj["mcon"]["met1"] = {"min_enclosure": 0.08}
grulesobj["mcon"]["via1"] = {}
grulesobj["mcon"]["met2"] = {}
grulesobj["mcon"]["via2"] = {}
grulesobj["mcon"]["met3"] = {}
grulesobj["mcon"]["via3"] = {}
grulesobj["mcon"]["met4"] = {}
grulesobj["mcon"]["via4"] = {}
grulesobj["mcon"]["met5"] = {}
grulesobj["mcon"]["capmet"] = {}
grulesobj["met1"]["dnwell"] = {}
grulesobj["met1"]["pwell"] = {}
grulesobj["met1"]["nwell"] = {}
grulesobj["met1"]["p+s/d"] = {}
grulesobj["met1"]["n+s/d"] = {}
grulesobj["met1"]["active_diff"] = {}
grulesobj["met1"]["active_tap"] = {}
grulesobj["met1"]["poly"] = {}
grulesobj["met1"]["mcon"] = {}
grulesobj["met1"]["met1"] = {"min_width": 0.17, "min_separation": 0.17}
grulesobj["met1"]["via1"] = {"min_enclosure": 0.0}
grulesobj["met1"]["met2"] = {}
grulesobj["met1"]["via2"] = {}
grulesobj["met1"]["met3"] = {}
grulesobj["met1"]["via3"] = {}
grulesobj["met1"]["met4"] = {}
grulesobj["met1"]["via4"] = {}
grulesobj["met1"]["met5"] = {}
grulesobj["met1"]["capmet"] = {}
grulesobj["via1"]["dnwell"] = {}
grulesobj["via1"]["pwell"] = {}
grulesobj["via1"]["nwell"] = {}
grulesobj["via1"]["p+s/d"] = {}
grulesobj["via1"]["n+s/d"] = {}
grulesobj["via1"]["active_diff"] = {}
grulesobj["via1"]["active_tap"] = {}
grulesobj["via1"]["poly"] = {}
grulesobj["via1"]["mcon"] = {}
grulesobj["via1"]["met1"] = {}
grulesobj["via1"]["via1"] = {"min_width": 0.17, "min_separation": 0.19, "width": 0.17}
grulesobj["via1"]["met2"] = {"min_enclosure": 0.06}
grulesobj["via1"]["via2"] = {}
grulesobj["via1"]["met3"] = {}
grulesobj["via1"]["via3"] = {}
grulesobj["via1"]["met4"] = {}
grulesobj["via1"]["via4"] = {}
grulesobj["via1"]["met5"] = {}
grulesobj["via1"]["capmet"] = {}
grulesobj["met2"]["dnwell"] = {}
grulesobj["met2"]["pwell"] = {}
grulesobj["met2"]["nwell"] = {}
grulesobj["met2"]["p+s/d"] = {}
grulesobj["met2"]["n+s/d"] = {}
grulesobj["met2"]["active_diff"] = {}
grulesobj["met2"]["active_tap"] = {}
grulesobj["met2"]["poly"] = {}
grulesobj["met2"]["mcon"] = {}
grulesobj["met2"]["met1"] = {}
grulesobj["met2"]["via1"] = {}
grulesobj["met2"]["met2"] = {"min_width": 0.14, "min_separation": 0.14}
grulesobj["met2"]["via2"] = {"min_enclosure": 0.14}
grulesobj["met2"]["met3"] = {}
grulesobj["met2"]["via3"] = {}
grulesobj["met2"]["met4"] = {}
grulesobj["met2"]["via4"] = {}
grulesobj["met2"]["met5"] = {}
grulesobj["met2"]["capmet"] = {}
grulesobj["via2"]["dnwell"] = {}
grulesobj["via2"]["pwell"] = {}
grulesobj["via2"]["nwell"] = {}
grulesobj["via2"]["p+s/d"] = {}
grulesobj["via2"]["n+s/d"] = {}
grulesobj["via2"]["active_diff"] = {}
grulesobj["via2"]["active_tap"] = {}
grulesobj["via2"]["poly"] = {}
grulesobj["via2"]["mcon"] = {}
grulesobj["via2"]["met1"] = {}
grulesobj["via2"]["via1"] = {}
grulesobj["via2"]["met2"] = {}
grulesobj["via2"]["via2"] = {"min_width": 0.21, "min_separation": 0.17, "width": 0.15}
grulesobj["via2"]["met3"] = {"min_enclosure": 0.09}
grulesobj["via2"]["via3"] = {}
grulesobj["via2"]["met4"] = {}
grulesobj["via2"]["via4"] = {}
grulesobj["via2"]["met5"] = {}
grulesobj["via2"]["capmet"] = {}
grulesobj["met3"]["dnwell"] = {}
grulesobj["met3"]["pwell"] = {}
grulesobj["met3"]["nwell"] = {}
grulesobj["met3"]["p+s/d"] = {}
grulesobj["met3"]["n+s/d"] = {}
grulesobj["met3"]["active_diff"] = {}
grulesobj["met3"]["active_tap"] = {}
grulesobj["met3"]["poly"] = {}
grulesobj["met3"]["mcon"] = {}
grulesobj["met3"]["met1"] = {}
grulesobj["met3"]["via1"] = {}
grulesobj["met3"]["met2"] = {}
grulesobj["met3"]["via2"] = {}
grulesobj["met3"]["met3"] = {"min_width": 0.14, "min_separation": 0.28}
grulesobj["met3"]["via3"] = {"min_enclosure":0.19}
grulesobj["met3"]["met4"] = {}
grulesobj["met3"]["via4"] = {}
grulesobj["met3"]["met5"] = {}
grulesobj["met3"]["capmet"] = {}
grulesobj["via3"]["dnwell"] = {}
grulesobj["via3"]["pwell"] = {}
grulesobj["via3"]["nwell"] = {}
grulesobj["via3"]["p+s/d"] = {}
grulesobj["via3"]["n+s/d"] = {}
grulesobj["via3"]["active_diff"] = {}
grulesobj["via3"]["active_tap"] = {}
grulesobj["via3"]["poly"] = {}
grulesobj["via3"]["mcon"] = {}
grulesobj["via3"]["met1"] = {}
grulesobj["via3"]["via1"] = {}
grulesobj["via3"]["met2"] = {}
grulesobj["via3"]["via2"] = {}
grulesobj["via3"]["met3"] = {}
grulesobj["via3"]["via3"] = {"min_width": 0.2, "min_separation": 0.2, "width": 0.2}
grulesobj["via3"]["met4"] = {"min_enclosure": 0.65}
grulesobj["via3"]["via4"] = {}
grulesobj["via3"]["met5"] = {}
grulesobj["via3"]["capmet"] = {}
grulesobj["met4"]["dnwell"] = {}
grulesobj["met4"]["pwell"] = {}
grulesobj["met4"]["nwell"] = {}
grulesobj["met4"]["p+s/d"] = {}
grulesobj["met4"]["n+s/d"] = {}
grulesobj["met4"]["active_diff"] = {}
grulesobj["met4"]["active_tap"] = {}
grulesobj["met4"]["poly"] = {}
grulesobj["met4"]["mcon"] = {}
grulesobj["met4"]["met1"] = {}
grulesobj["met4"]["via1"] = {}
grulesobj["met4"]["met2"] = {}
grulesobj["met4"]["via2"] = {}
grulesobj["met4"]["met3"] = {}
grulesobj["met4"]["via3"] = {}
grulesobj["met4"]["met4"] = {"min_width": 0.3, "min_separation": 0.4}
grulesobj["met4"]["via4"] = {"min_enclosure": 0.09}
grulesobj["met4"]["met5"] = {}
grulesobj["met4"]["capmet"] = {"min_enclosure": 0.14}
grulesobj["via4"]["dnwell"] = {}
grulesobj["via4"]["pwell"] = {}
grulesobj["via4"]["nwell"] = {}
grulesobj["via4"]["p+s/d"] = {}
grulesobj["via4"]["n+s/d"] = {}
grulesobj["via4"]["active_diff"] = {}
grulesobj["via4"]["active_tap"] = {}
grulesobj["via4"]["poly"] = {}
grulesobj["via4"]["mcon"] = {}
grulesobj["via4"]["met1"] = {}
grulesobj["via4"]["via1"] = {}
grulesobj["via4"]["met2"] = {}
grulesobj["via4"]["via2"] = {}
grulesobj["via4"]["met3"] = {}
grulesobj["via4"]["via3"] = {}
grulesobj["via4"]["met4"] = {}
grulesobj["via4"]["via4"] = {"width": 0.2, "min_separation": 0.35}
grulesobj["via4"]["met5"] = {"min_enclosure": 0.07}
grulesobj["via4"]["capmet"] = {}
grulesobj["met5"]["dnwell"] = {}
grulesobj["met5"]["pwell"] = {}
grulesobj["met5"]["nwell"] = {}
grulesobj["met5"]["p+s/d"] = {}
grulesobj["met5"]["n+s/d"] = {}
grulesobj["met5"]["active_diff"] = {}
grulesobj["met5"]["active_tap"] = {}
grulesobj["met5"]["poly"] = {}
grulesobj["met5"]["mcon"] = {}
grulesobj["met5"]["met1"] = {}
grulesobj["met5"]["via1"] = {}
grulesobj["met5"]["met2"] = {}
grulesobj["met5"]["via2"] = {}
grulesobj["met5"]["met3"] = {}
grulesobj["met5"]["via3"] = {}
grulesobj["met5"]["met4"] = {}
grulesobj["met5"]["via4"] = {}
grulesobj["met5"]["met5"] = {"min_width": 0.3, "min_separation": 0.4}
grulesobj["met5"]["capmet"] = {}
grulesobj["capmet"]["dnwell"] = {}
grulesobj["capmet"]["pwell"] = {}
grulesobj["capmet"]["nwell"] = {}
grulesobj["capmet"]["p+s/d"] = {}
grulesobj["capmet"]["n+s/d"] = {}
grulesobj["capmet"]["active_diff"] = {}
grulesobj["capmet"]["active_tap"] = {}
grulesobj["capmet"]["poly"] = {}
grulesobj["capmet"]["mcon"] = {}
grulesobj["capmet"]["met1"] = {}
grulesobj["capmet"]["via1"] = {}
grulesobj["capmet"]["met2"] = {}
grulesobj["capmet"]["via2"] = {}
grulesobj["capmet"]["met3"] = {}
grulesobj["capmet"]["via3"] = {}
grulesobj["capmet"]["met4"] = {}
grulesobj["capmet"]["via4"] = {}
grulesobj["capmet"]["met5"] = {}
grulesobj["capmet"]["capmet"] = {"capmettop": (71, 20), "capmetbottom": (70, 20), "min_separation": 1.2}



# PDK file paths
pdk_root = Path('/usr/bin/miniconda3/share/pdk/')
klayout_drc_file = Path(__file__).parent / "sky130_drc.lydrc"
lvs_schematic_ref_file = pdk_root / "sky130A" / "libs.ref" / "sky130_fd_sc_hd" / "spice" / "sky130_fd_sc_hd.spice"
lvs_setup_tcl_file = pdk_root / "sky130A" / "libs.tech" / "netgen" / "sky130_setup.tcl"
magic_drc_file = pdk_root / "sky130A" / "libs.tech" / "magic" / "sky130A.magicrc"
temp_dir = None

# Setup PDK files
pdk_files = SetupPDKFiles(
    pdk_root=pdk_root,
    klayout_drc_file=klayout_drc_file,
    lvs_schematic_ref_file=lvs_schematic_ref_file,
    lvs_setup_tcl_file=lvs_setup_tcl_file,
    magic_drc_file=magic_drc_file,
    temp_dir=temp_dir,
    pdk='sky130'
).return_dict_of_files()




LAYER = {
    "met5": (68, 20),
    "via4": (67, 44),
    "met4": (66, 20),
    "via3": (65, 44),
    "met3": (64, 20),
    "via2": (63, 44),
    "met2": (62, 20),
    "via1": (61, 44),
    "met1": (60, 20),
    "mcon": (66, 44),
    "poly": (66, 20),
    "active": (65, 20),
    "n+s/d": (64, 20),
    "p+s/d": (64, 44),
    "nwell": (64, 20),
    "dnwell": (64, 44),
    "capmet": (89, 44),
    # Label layers
    "met5_label": (68, 10),
    "met4_label": (66, 10),
    "met3_label": (64, 10),
    "met2_label": (62, 10),
    "met1_label": (60, 10),
    "poly_label": (66, 10),
    "active_label": (65, 10),
}


sky130_glayer_mapping = {
    "met5": "met5",
    "via4": "via4",
    "met4": "met4",
    "via3": "via3",
    "met3": "met3",
    "via2": "via2",
    "met2": "met2",
    "via1": "via1",
    "met1": "met1",
    "mcon": "mcon",
    "poly": "poly",
    "active_diff": "active",
    "active_tap": "active",
    "n+s/d": "n+s/d",
    "p+s/d": "p+s/d",
    "nwell": "nwell",
    "dnwell": "dnwell",
    "capmet": "capmet",
    # Pin layers
    "met5_pin": "met5_label",
    "met4_pin": "met4_label",
    "met3_pin": "met3_label",
    "met2_pin": "met2_label",
    "met1_pin": "met1_label",
    "poly_pin": "poly_label",
    "active_diff_pin": "active_label",
    # Label layers
    "met5_label": "met5_label",
    "met4_label": "met4_label",
    "met3_label": "met3_label",
    "met2_label": "met2_label",
    "met1_label": "met1_label",
    "poly_label": "poly_label",
    "active_diff_label": "active_label",
}


sky130_mapped_pdk = MappedPDK(
    name="sky130",
    glayers=sky130_glayer_mapping,
    models={
        "nfet": "sky130_fd_pr__nfet_01v8",
        "pfet": "sky130_fd_pr__pfet_01v8",
        "mimcap": "sky130_fd_pr__cap_mim_m3_1"
    },
    layers=LAYER,
    grules=grulesobj,
    pdk_files=pdk_files,
    default_decorator=sky130_add_npc,
)