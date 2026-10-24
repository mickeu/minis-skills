
/var/minis/skills/iflytek-analysis/references/backup_bin/ProcessStroke.bin:     file format binary


Disassembly of section .data:

000000010102a5d4 <.data>:
   10102a5d4:	d10343ff 	sub	sp, sp, #0xd0
   10102a5d8:	a9076ffc 	stp	x28, x27, [sp, #112]
   10102a5dc:	a90867fa 	stp	x26, x25, [sp, #128]
   10102a5e0:	a9095ff8 	stp	x24, x23, [sp, #144]
   10102a5e4:	a90a57f6 	stp	x22, x21, [sp, #160]
   10102a5e8:	a90b4ff4 	stp	x20, x19, [sp, #176]
   10102a5ec:	a90c7bfd 	stp	x29, x30, [sp, #192]
   10102a5f0:	910303fd 	add	x29, sp, #0xc0
   10102a5f4:	a9058fe0 	stp	x0, x3, [sp, #88]
   10102a5f8:	aa0203f7 	mov	x23, x2
   10102a5fc:	aa0103fa 	mov	x26, x1
   10102a600:	f9400b40 	ldr	x0, [x26, #16]
   10102a604:	f9400008 	ldr	x8, [x0]
   10102a608:	f9402908 	ldr	x8, [x8, #80]
   10102a60c:	d63f0100 	blr	x8
   10102a610:	aa0003f8 	mov	x24, x0
   10102a614:	f9401740 	ldr	x0, [x26, #40]
   10102a618:	b40004a0 	cbz	x0, 0x10102a6ac
   10102a61c:	f9400708 	ldr	x8, [x24, #8]
   10102a620:	a9416513 	ldp	x19, x25, [x8, #16]
   10102a624:	f9401b55 	ldr	x21, [x26, #48]
   10102a628:	f9400008 	ldr	x8, [x0]
   10102a62c:	f9402908 	ldr	x8, [x8, #80]
   10102a630:	d63f0100 	blr	x8
   10102a634:	aa0003f6 	mov	x22, x0
   10102a638:	f9401ac0 	ldr	x0, [x22, #48]
   10102a63c:	f94006fb 	ldr	x27, [x23, #8]
   10102a640:	f9400374 	ldr	x20, [x27]
   10102a644:	f9400ea8 	ldr	x8, [x21, #24]
   10102a648:	b4000068 	cbz	x8, 0x10102a654
   10102a64c:	b9400108 	ldr	w8, [x8]
   10102a650:	12005d08 	and	w8, w8, #0xffffff
   10102a654:	a940ab09 	ldp	x9, x10, [x24, #8]
   10102a658:	f9002bea 	str	x10, [sp, #80]
   10102a65c:	b9400129 	ldr	w9, [x9]
   10102a660:	b8685a6a 	ldr	w10, [x19, w8, uxtw #2]
   10102a664:	5301615c 	ubfx	w28, w10, #1, #24
   10102a668:	1100050a 	add	w10, w8, #0x1
   10102a66c:	b86a5a6a 	ldr	w10, [x19, w10, uxtw #2]
   10102a670:	53016157 	ubfx	w23, w10, #1, #24
   10102a674:	6b09011f 	cmp	w8, w9
   10102a678:	540006e1 	b.ne	0x10102a754  // b.any
   10102a67c:	f9400408 	ldr	x8, [x0, #8]
   10102a680:	b4002f48 	cbz	x8, 0x10102ac68
   10102a684:	b9400749 	ldr	w9, [x26, #4]
   10102a688:	d100050a 	sub	x10, x8, #0x1
   10102a68c:	ea08014b 	ands	x11, x10, x8
   10102a690:	54001e60 	b.eq	0x10102aa5c  // b.none
   10102a694:	aa0903ec 	mov	x12, x9
   10102a698:	eb09011f 	cmp	x8, x9
   10102a69c:	54001e28 	b.hi	0x10102aa60  // b.pmore
   10102a6a0:	9ac8092c 	udiv	x12, x9, x8
   10102a6a4:	9b08a58c 	msub	x12, x12, x8, x9
   10102a6a8:	140000ee 	b	0x10102aa60
   10102a6ac:	5290d474 	mov	w20, #0x86a3                	// #34467
   10102a6b0:	72a00034 	movk	w20, #0x1, lsl #16
   10102a6b4:	b0012013 	adrp	x19, 0x10342b000
   10102a6b8:	f9473260 	ldr	x0, [x19, #3680]
   10102a6bc:	b4002d80 	cbz	x0, 0x10102ac6c
   10102a6c0:	b9404c08 	ldr	w8, [x0, #76]
   10102a6c4:	34000168 	cbz	w8, 0x10102a6f0
   10102a6c8:	39414008 	ldrb	w8, [x0, #80]
   10102a6cc:	36080128 	tbz	w8, #1, 0x10102a6f0
   10102a6d0:	b000a168 	adrp	x8, 0x102457000
   10102a6d4:	912c2d08 	add	x8, x8, #0xb0b
   10102a6d8:	f90003e8 	str	x8, [sp]
   10102a6dc:	b000a161 	adrp	x1, 0x102457000
   10102a6e0:	912bac21 	add	x1, x1, #0xaeb
   10102a6e4:	97fa89f5 	bl	0x100ecceb8
   10102a6e8:	f9473260 	ldr	x0, [x19, #3680]
   10102a6ec:	b4000160 	cbz	x0, 0x10102a718
   10102a6f0:	b9404c08 	ldr	w8, [x0, #76]
   10102a6f4:	34000128 	cbz	w8, 0x10102a718
   10102a6f8:	39414008 	ldrb	w8, [x0, #80]
   10102a6fc:	360800e8 	tbz	w8, #1, 0x10102a718
   10102a700:	b000a168 	adrp	x8, 0x102457000
   10102a704:	9111e508 	add	x8, x8, #0x479
   10102a708:	a90053e8 	stp	x8, x20, [sp]
   10102a70c:	9000a1a1 	adrp	x1, 0x10245e000
   10102a710:	91160021 	add	x1, x1, #0x580
   10102a714:	97fa89e9 	bl	0x100ecceb8
   10102a718:	f9401748 	ldr	x8, [x26, #40]
   10102a71c:	b5002a88 	cbnz	x8, 0x10102ac6c
   10102a720:	f9473260 	ldr	x0, [x19, #3680]
   10102a724:	b4002a40 	cbz	x0, 0x10102ac6c
   10102a728:	b9404c08 	ldr	w8, [x0, #76]
   10102a72c:	34002a08 	cbz	w8, 0x10102ac6c
   10102a730:	39414008 	ldrb	w8, [x0, #80]
   10102a734:	360029c8 	tbz	w8, #0, 0x10102ac6c
   10102a738:	b000a168 	adrp	x8, 0x102457000
   10102a73c:	912c2d08 	add	x8, x8, #0xb0b
   10102a740:	f90003e8 	str	x8, [sp]
   10102a744:	f000a101 	adrp	x1, 0x10244d000
   10102a748:	910bf021 	add	x1, x1, #0x2fc
   10102a74c:	97fa8a67 	bl	0x100ecd0e8
   10102a750:	14000147 	b	0x10102ac6c
   10102a754:	6b17039f 	cmp	w28, w23
   10102a758:	54002882 	b.cs	0x10102ac68  // b.hs, b.nlast
   10102a75c:	321f07e9 	orr	w9, wzr, #0x6
   10102a760:	9ba966f3 	umaddl	x19, w23, w9, x25
   10102a764:	f94006c8 	ldr	x8, [x22, #8]
   10102a768:	f9401117 	ldr	x23, [x8, #32]
   10102a76c:	320107f4 	mov	w20, #0x80000001            	// #-2147483647
   10102a770:	9ba96798 	umaddl	x24, w28, w9, x25
   10102a774:	5280213c 	mov	w28, #0x109                 	// #265
   10102a778:	14000002 	b	0x10102a780
   10102a77c:	f94006c8 	ldr	x8, [x22, #8]
   10102a780:	f9400908 	ldr	x8, [x8, #16]
   10102a784:	aa1803f9 	mov	x25, x24
   10102a788:	78404f25 	ldrh	w5, [x25, #4]!
   10102a78c:	f9400f69 	ldr	x9, [x27, #24]
   10102a790:	b40003a9 	cbz	x9, 0x10102a804
   10102a794:	78657908 	ldrh	w8, [x8, x5, lsl #1]
   10102a798:	aa2803e9 	mvn	x9, x8
   10102a79c:	8b085529 	add	x9, x9, x8, lsl #21
   10102a7a0:	ca496129 	eor	x9, x9, x9, lsr #24
   10102a7a4:	9b1c7d29 	mul	x9, x9, x28
   10102a7a8:	ca493929 	eor	x9, x9, x9, lsr #14
   10102a7ac:	528002aa 	mov	w10, #0x15                  	// #21
   10102a7b0:	9b0a7d29 	mul	x9, x9, x10
   10102a7b4:	ca497129 	eor	x9, x9, x9, lsr #28
   10102a7b8:	9b147d29 	mul	x9, x9, x20
   10102a7bc:	f9400b6a 	ldr	x10, [x27, #16]
   10102a7c0:	d100054b 	sub	x11, x10, #0x1
   10102a7c4:	8a0b012c 	and	x12, x9, x11
   10102a7c8:	f9401b6a 	ldr	x10, [x27, #48]
   10102a7cc:	f86c794a 	ldr	x10, [x10, x12, lsl #3]
   10102a7d0:	b40001aa 	cbz	x10, 0x10102a804
   10102a7d4:	f940014a 	ldr	x10, [x10]
   10102a7d8:	b400016a 	cbz	x10, 0x10102a804
   10102a7dc:	f940054d 	ldr	x13, [x10, #8]
   10102a7e0:	eb0901bf 	cmp	x13, x9
   10102a7e4:	540000a1 	b.ne	0x10102a7f8  // b.any
   10102a7e8:	7940214d 	ldrh	w13, [x10, #16]
   10102a7ec:	6b0d011f 	cmp	w8, w13
   10102a7f0:	54ffff21 	b.ne	0x10102a7d4  // b.any
   10102a7f4:	14000026 	b	0x10102a88c
   10102a7f8:	8a0b01ad 	and	x13, x13, x11
   10102a7fc:	eb0c01bf 	cmp	x13, x12
   10102a800:	54fffea0 	b.eq	0x10102a7d4  // b.none
   10102a804:	f94006e8 	ldr	x8, [x23, #8]
   10102a808:	b4001228 	cbz	x8, 0x10102aa4c
   10102a80c:	d1000509 	sub	x9, x8, #0x1
   10102a810:	ea08012a 	ands	x10, x9, x8
   10102a814:	540000e0 	b.eq	0x10102a830  // b.none
   10102a818:	aa0503eb 	mov	x11, x5
   10102a81c:	eb05011f 	cmp	x8, x5
   10102a820:	540000a8 	b.hi	0x10102a834  // b.pmore
   10102a824:	9ac808ab 	udiv	x11, x5, x8
   10102a828:	9b08956b 	msub	x11, x11, x8, x5
   10102a82c:	14000002 	b	0x10102a834
   10102a830:	8a05012b 	and	x11, x9, x5
   10102a834:	f94002ec 	ldr	x12, [x23]
   10102a838:	f86b798c 	ldr	x12, [x12, x11, lsl #3]
   10102a83c:	b400108c 	cbz	x12, 0x10102aa4c
   10102a840:	f940018c 	ldr	x12, [x12]
   10102a844:	b400104c 	cbz	x12, 0x10102aa4c
   10102a848:	f940058d 	ldr	x13, [x12, #8]
   10102a84c:	eb0501bf 	cmp	x13, x5
   10102a850:	540000a1 	b.ne	0x10102a864  // b.any
   10102a854:	7940218d 	ldrh	w13, [x12, #16]
   10102a858:	6b0501bf 	cmp	w13, w5
   10102a85c:	54ffff21 	b.ne	0x10102a840  // b.any
   10102a860:	14000024 	b	0x10102a8f0
   10102a864:	b40000ca 	cbz	x10, 0x10102a87c
   10102a868:	eb0801bf 	cmp	x13, x8
   10102a86c:	540000a3 	b.cc	0x10102a880  // b.lo, b.ul, b.last
   10102a870:

...

02ab20:	a9402928 	ldp	x8, x10, [x9]
   10102ab24:	f90023e9 	str	x9, [sp, #64]
   10102ab28:	cb080149 	sub	x9, x10, x8
   10102ab2c:	d343fd2b 	lsr	x11, x9, #3
   10102ab30:	7100057f 	cmp	w11, #0x1
   10102ab34:	5400082b 	b.lt	0x10102ac38  // b.tstop
   10102ab38:	eb08015f 	cmp	x10, x8
   10102ab3c:	54000aa0 	b.eq	0x10102ac90  // b.none
   10102ab40:	d2800013 	mov	x19, #0x0                   	// #0
   10102ab44:	93438929 	sbfx	x9, x9, #3, #32
   10102ab48:	f90027e9 	str	x9, [sp, #72]
   10102ab4c:	f8737918 	ldr	x24, [x8, x19, lsl #3]
   10102ab50:	79403308 	ldrh	w8, [x24, #24]
   10102ab54:	f9401fe9 	ldr	x9, [sp, #56]
   10102ab58:	8b080529 	add	x9, x9, x8, lsl #1
   10102ab5c:	79400128 	ldrh	w8, [x9]
   10102ab60:	79400529 	ldrh	w9, [x9, #2]
   10102ab64:	6b09011f 	cmp	w8, w9
   10102ab68:	54000522 	b.cs	0x10102ac0c  // b.hs, b.nlast
   10102ab6c:	f9401bea 	ldr	x10, [sp, #48]
   10102ab70:	8b08095a 	add	x26, x10, x8, lsl #2
   10102ab74:	cb080136 	sub	x22, x9, x8
   10102ab78:	b9400348 	ldr	w8, [x26]
   10102ab7c:	6b1c011f 	cmp	w8, w28
   10102ab80:	7a572102 	ccmp	w8, w23, #0x2, cs	// cs = hs, nlast
   10102ab84:	540003e2 	b.cs	0x10102ac00  // b.hs, b.nlast
   10102ab88:	9bbb6506 	umaddl	x6, w8, w27, x25
   10102ab8c:	b94000c9 	ldr	w9, [x6]
   10102ab90:	92405d2a 	and	x10, x9, #0xffffff
   10102ab94:	f9402beb 	ldr	x11, [sp, #80]
   10102ab98:	38ea696a 	ldrsb	w10, [x11, x10]
   10102ab9c:	f9402feb 	ldr	x11, [sp, #88]
   10102aba0:	f9400960 	ldr	x0, [x11, #16]
   10102aba4:	39401283 	ldrb	w3, [x20, #4]
   10102aba8:	d3587d24 	ubfx	x4, x9, #24, #8
   10102abac:	9b1b7d08 	mul	x8, x8, x27
   10102abb0:	8b080328 	add	x8, x25, x8
   10102abb4:	79400905 	ldrh	w5, [x8, #4]
   10102abb8:	f90003f5 	str	x21, [sp]
   10102abbc:	12003d41 	and	w1, w10, #0xffff
   10102abc0:	320003e2 	orr	w2, wzr, #0x1
   10102abc4:	aa1803e7 	mov	x7, x24
   10102abc8:	97fff63a 	bl	0x1010284b0
   10102abcc:	f81a83a0 	stur	x0, [x29, #-88]
   10102abd0:	f94033ea 	ldr	x10, [sp, #96]
   10102abd4:	a940a548 	ldp	x8, x9, [x10, #8]
   10102abd8:	eb09011f 	cmp	x8, x9
   10102abdc:	540000c0 	b.eq	0x10102abf4  // b.none
   10102abe0:	f9000100 	str	x0, [x8]
   10102abe4:	f9400548 	ldr	x8, [x10, #8]
   10102abe8:	91002108 	add	x8, x8, #0x8
   10102abec:	f9000548 	str	x8, [x10, #8]
   10102abf0:	14000004 	b	0x10102ac00
   10102abf4:	d10163a1 	sub	x1, x29, #0x58
   10102abf8:	aa0a03e0 	mov	x0, x10
   10102abfc:	97fff41a 	bl	0x101027c64
   10102ac00:	9100135a 	add	x26, x26, #0x4
   10102ac04:	f10006d6 	subs	x22, x22, #0x1
   10102ac08:	54fffb81 	b.ne	0x10102ab78  // b.any
   10102ac0c:	91000673 	add	x19, x19, #0x1
   10102ac10:	f94027e8 	ldr	x8, [sp, #72]
   10102ac14:	eb08027f 	cmp	x19, x8
   10102ac18:	5400010a 	b.ge	0x10102ac38  // b.tcont
   10102ac1c:	f94023e9 	ldr	x9, [sp, #64]
   10102ac20:	a9402528 	ldp	x8, x9, [x9]
   10102ac24:	cb080129 	sub	x9, x9, x8
   10102ac28:	9343fd29 	asr	x9, x9, #3
   10102ac2c:	eb13013f 	cmp	x9, x19
   10102ac30:	54fff8e8 	b.hi	0x10102ab4c  // b.pmore
   10102ac34:	14000017 	b	0x10102ac90
   10102ac38:	a9422be8 	ldp	x8, x10, [sp, #32]
   10102ac3c:	9100054a 	add	x10, x10, #0x1
   10102ac40:	eb08015f 	cmp	x10, x8
   10102ac44:	5400012a 	b.ge	0x10102ac68  // b.tcont
   10102ac48:	f9400fe9 	ldr	x9, [sp, #24]
   10102ac4c:	a9402528 	ldp	x8, x9, [x9]
   10102ac50:	cb080129 	sub	x9, x9, x8
   10102ac54:	9343fd29 	asr	x9, x9, #3
   10102ac58:	eb0a013f 	cmp	x9, x10
   10102ac5c:	54fff568 	b.hi	0x10102ab08  // b.pmore
   10102ac60:	f9400fe0 	ldr	x0, [sp, #24]
   10102ac64:	944598ae 	bl	0x102190f1c
   10102ac68:	52800014 	mov	w20, #0x0                   	// #0
   10102ac6c:	aa1403e0 	mov	x0, x20
   10102ac70:	a94c7bfd 	ldp	x29, x30, [sp, #192]
   10102ac74:	a94b4ff4 	ldp	x20, x19, [sp, #176]
   10102ac78:	a94a57f6 	ldp	x22, x21, [sp, #160]
   10102ac7c:	a9495ff8 	ldp	x24, x23, [sp, #144]
   10102ac80:	a94867fa 	ldp	x26, x25, [sp, #128]
   10102ac84:	a9476ffc 	ldp	x28, x27, [sp, #112]
   10102ac88:	910343ff 	add	sp, sp, #0xd0
   10102ac8c:	d65f03c0 	ret
   10102ac90:	f94023e0 	ldr	x0, [sp, #64]
   10102ac94:	944598a2 	bl	0x102190f1c
   10102ac98:	d103c3ff 	sub	sp, sp, #0xf0
   10102ac9c:	a9096ffc 	stp	x28, x27, [sp, #144]
   10102aca0:	a90a67fa 	stp	x26, x25, [sp, #160]
   10102aca4:	a90b5ff8 	stp	x24, x23, [sp, #176]
   10102aca8:	a90c57f6 	stp	x22, x21, [sp, #192]
   10102acac:	a90d4ff4 	stp	x20, x19, [sp, #208]
   10102acb0:	a90e7bfd 	stp	x29, x30, [sp, #224]
   10102acb4:	910383fd 	add	x29, sp, #0xe0
   10102acb8:	f81983a3 	stur	x3, [x29, #-104]
   10102acbc:	aa0203f6 	mov	x22, x2
   10102acc0:	aa0103f5 	mov	x21, x1
   10102acc4:	f9003be0 	str	x0, [sp, #112]
   10102acc8:	f9400aa0 	ldr	x0, [x21, #16]
   10102accc:	f9400008 	ldr	x8, [x0]
   10102acd0:	f9402908 	ldr	x8, [x8, #80]
   10102acd4:	d63f0100 	blr	x8
   10102acd8:	aa0003f9 	mov	x25, x0
   10102acdc:	f94016a0 	ldr	x0, [x21, #40]
   10102ace0:	b40005a0 	cbz	x0, 0x10102ad94
   10102ace4:	f9400728 	ldr	x8, [x25, #8]
   10102ace8:	a9416914 	ldp	x20, x26, [x8, #16]
   10102acec:	f9401ab7 	ldr	x23, [x21, #48]
   10102acf0:	f94006fb 	ldr	x27, [x23, #8]
   10102acf4:	f9400008 	ldr	x8, [x0]
   10102acf8:	f9402908 	ldr	x8, [x8, #80]
   10102acfc:	d63f0100 	blr	x8
   10102ad00:	aa0003f8 	mov	x24, x0
   10102ad04:	f9401b00 	ldr	x0, [x24, #48]
   10102ad08:	f9400728 	ldr	x8, [x25, #8]
   10102ad0c:	f9401513 	ldr	x19, [x8, #40]
   10102ad10:	f90033f5 	str	x21, [sp, #96]
   10102ad14:	b94006a9 	ldr	w9, [x21, #4]
   10102ad18:	f9002be9 	str	x9, [sp, #80]
   10102ad1c:	39404ad5 	ldrb	w21, [x22, #18]
   10102ad20:	f94006c9 	ldr	x9, [x22, #8]
   10102ad24:	f940053c 	ldr	x28, [x9, #8]
   10102ad28:	aa1c03eb 	mov	x11, x28
   10102ad2c:	f8408576 	ldr	x22, [x11], #8
   10102ad30:	f9400ee9 	ldr	x9, [x23, #24]
   10102ad34:	b4000069 	cbz	x9, 0x10102ad40
   10102ad38:	b9400129 	ldr	w9, [x9]
   10102ad3c:	12005d29 	and	w9, w9, #0xffffff
   10102ad40:	f9400b2a 	ldr	x10, [x25, #16]
   10102ad44:	f90037ea 	str	x10, [sp, #104]
   10102ad48:	b9400108 	ldr	w8, [x8]
   10102ad4c:	b8695a8a 	ldr	w10, [x20, w9, uxtw #2]
   10102ad50:	53016159 	ubfx	w25, w10, #1, #24
   10102ad54:	6b08013f 	cmp	w9, w8
   10102ad58:	54000721 	b.ne	0x10102ae3c  // b.any
   10102ad5c:	f9400408 	ldr	x8, [x0, #8]
   10102ad60:	b4004ea8 	cbz	x8, 0x10102b734
   10102ad64:	11000529 	add	w9, w9, #0x1
   10102ad68:	b8695a8d 	ldr	w13, [x20, w9, uxtw #2]
   10102ad6c:	d1000509 	sub	x9, x8, #0x1
   10102ad70:	ea08012a 	ands	x10, x9, x8
   10102ad74:	54003780 	b.eq	0x10102b464  // b.none
   10102ad78:	f9402bf3 	ldr	x19, [sp, #80]
   10102ad7c:	aa1303eb 	mov	x11, x19
   10102ad80:	eb13011f 	cmp	x8, x19
   10102ad84:	54003748 	b.hi	0x10102b46c  // b.pmore
   10102ad88:	9ac80a6b 	udiv	x11, x19, x8
   10102ad8c:	9b08cd6b 	msub	x11, x11, x8, x19
   10102ad90:	140001b7 	b	0x10102b46c
   10102ad94:	5290d474 	mov	w20, #0x86a3                	// #34467
   10102ad98:	72a00034 	movk	w20, #0x1, lsl #16
   10102ad9c:	b0012013 	adrp	x19, 0x10342b000
   10102ada0:	f9473260 	ldr	x0, [x19, #3680]
   10102ada4:	b4004ca0 	cbz	x0, 0x10102b738
   10102ada8:	b9404c08 	ldr	w8, [x0, #76]
   10102adac:	34000168 	cbz	w8, 0x10102add8
   10102adb0:	39414008 	ldrb	w8, [x0, #80]
   10102adb4:	36080128 	tbz	w8, #1, 0x10102add8
   10102adb8:	b000a168 	adrp	x8, 0x102457000
   10102adbc:	912c6508 	add	x8, x8, #0xb19
   10102adc0:	f90003e8 	str	x8, [sp]
   10102adc4:	b000a161 	adrp	x1, 0x102457000
   10102adc8:	912bac21 	add	x1, x1, #0xaeb
   10102adcc:	97fa883b 	bl	0x100ecceb8
   10102add0:	f9473260 	ldr	x0, [x19, #3680]


[OUTPUT TRUNCATED] Showing first & last 7500 of 22351 chars (520 lines total).
Use file_read tool to read specific sections.