В основном все дистрибутивы делятся на три основные семейства:
- Red Hat Family Systems. CentOS и Fedora
	Особенности:
	1. Все основные инновационные шняги здесь
	2. Идут на самых уникальных конфигурациях ПК
	3. Использует yum package manager
	4. Распространен в компаниях
- SUSE Family Systems. OpenSUSE
	Особенности:
	1. SLES(дистрибутив для сервера) на нём.
	2. RPM-based zypper package manager
	3. YaST for system admin
	4. Используется во множестве отраслей
- Debian Family Systems. Ubuntu и Linux Mint
	Особенности:
	 1. DPKG-based APT package manager
	 2. Очень стабильное
	 3. GNOME-based

Linux borrows much from UNIX.
Linux acces features from files.

Linux Kernel contain:
- Package updates, upgrade Kernel and driver patches
- Support services: Commercial, community
- Documentation
- Libraries, utilites, configuration
- Applications 

Steps of power on linux:
1. Power on
2. BIOS(Basic Input/Output System). It initialize hardware, screen, keyboard and test memory. That step called post power on self-test. BIOS is stored on ROM chip on motherboard.
3. Master Boot Recorder(MBR). The control from BIOS transfer to boot loader Boot loader is stored in hard disk in the boot sector(first sector of hard disk or master boot). Size of MBR is 512 bytes. Machine does not acess to mass storage media. The most important information about computer(daya etc) is loaded from CMOS(chip, which save information in power off state). Exists: grub, ISO Linux, u-boot. Boot loader responsible for loading kernel image and initial RAM disk or file system into memory.  

Boot loader has two stages: 
	1. Find a bootable sector of memory. Looding second part of bootloader in RAM(for example GRUB)
	2. Then it give choice which system need to boot. Then it start kernel of the selected operating system and load it in the RAM. 

The file system contain a kernel functionality and drivers(udev system). After finding root files program check integrity and say a operating system, that a file system ready to use.
initramfs contain programs and binary files responsible for:
- mount proper root file system
- providing kernel functionality
- locating device
- locating drivers and load them 
- checking for errors  

Near the end of boot process it give abillity to write username and password and command shell(if we don't use gui).

Bootloader loads the kernel and initial ram-based file system into memory, so it can be used by kernel. When kernel downloaded, that is configures computer memory and devices. Also kernel download some applications.

After kernel did last step it runs /sbin/init(parent process), which start other processes. Also it responsible for keeping system running and shouttting down it clearly. That can be traditionally UNIX System V or systemd.
Systems with systemd startup faster than others, because use parallelisation instead of serilisation procesess. Startup shell scripts are replaced with simple configuration files 

Partition that is section in disk memory
File system is a method of storing or finding file in hard disk ![[Linux — media 1.png]]

Linux systems according their important files according FHS(Filesystem Hierarchy Standard):
- Linux use slash as separator(not backslash)
- It hasn't got letters for disk
- Sensitivity to caps

X window system loaded in the last step of boot process. 
Services of x window usually called X clients

Desktop enviroment(for example GNOME) consist:
- Session manager(mantain components of the session)
- Window manager(placement and movement)