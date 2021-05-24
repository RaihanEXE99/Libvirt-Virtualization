import libvirt

pool = "default" # Pool name

conn = libvirt.open("qemu+ssh://username@hostname/system")
if not conn:
    raise SystemExit("Failed to open connection to qemu:///system")

pool = conn.storagePoolLookupByName(pool)
if not pool:
    raise SystemExit("Failed to locate any StoragePool objects.")

stgvol = pool.listAllVolumes()

deleteThis = "sparse.img" #desired vol name

for vol in stgvol:
    if vol.name() == deleteThis:
        vol.wipe()
        vol.delete()
        
conn.close()
