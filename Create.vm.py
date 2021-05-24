import libvirt

pool = "default"

conn = libvirt.open("qemu+ssh://username@hostname/system")
if not conn:
    raise SystemExit("Failed to open connection to qemu:///system")

pool = conn.storagePoolLookupByName(pool)
if not pool:
    raise SystemExit("Failed to locate any StoragePool objects.")


stgvol_xml = """
<volume>
  <name>{}</name>
  <allocation>{}</allocation>
  <capacity unit="M">{}</capacity>
  <target>
    <path>/var/lib/libvirt/images/sparse.img</path>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>""".format("hello","0","20")


stgvol = pool.createXML(stgvol_xml, 0)
if not stgvol:
    raise SystemExit("Failed to create a  StorageVol objects.")

conn.close()
