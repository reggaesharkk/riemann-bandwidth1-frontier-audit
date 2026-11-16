# WP84 — fixed-band lower moments collapse to one variance parameter

Date: 2026-10-05

Status: **LOWER-MOMENT DEBT FOR THE QUARTIC FIRST STRIKE REDUCED TO THE BAND-TRUNCATED PRIME-PAIR VARIANCE**

No unconditional zero-density percentage is claimed here.

After scalar background reduction write H_R=I+P_R up to the already-closed o(1) normalized errors. Define v_R=tau(P_R^2). Then

    mu1(H_R)=1+o(1),
    mu2(H_R)=1+v_R+o(1).

The fixed-band degree-three sign-balance / unique-factorization gate removes the P_R^3 term, equivalently preserving the local identity O3(0,+u,-u)=O2(+u,-u). Hence

    boxed:
    mu3(H_R)=1+3v_R+o(1).

Thus the first three moments are controlled by one scalar v_R.

Let P=P_R+Delta_R, with P_R and Delta_R supported on disjoint matrix displacements. Since the sharp matrices are real symmetric,

    tau(P^2)=tau(P_R^2)+tau(Delta_R^2).

The full prime-pair variance is 1/3+o(1), while the displacement-tail theorem gives

    tau(Delta_R^2)<=2/(pi^2 R)+o(1).

Therefore

    1/3-2/(pi^2 R)+o(1) <= v_R <=1/3+o(1).

For the exact quartic majorant

    P4=(593/2000)x^4-(212/125)x^3+(1761/500)x^2-(3133/1000)x+1011/1000,

the lower-degree terms simplify exactly to

    tau P4(H_R)
      =(593/2000)mu4(H_R)-37/125-(783/500)v_R+o(1).

If mu4(H_R)=13/4+delta4 and delta_v=1/3-v_R, then

    tau P4(H_R)
      <=233/1600+(593/2000)delta4+(783/500)delta_v+o(1).

Using delta_v<=2/(pi^2R)+o(1),

    boxed:
    tau P4(H_R)
      <=233/1600+(593/2000)delta4+783/(250 pi^2 R)+o(1).

The extra lower-moment band constant is

    C_low=783/(250 pi^2) ~=0.3173379472.

Combining with the matched-filter full-to-band constant C_match~=2.1728342265 gives effective band constant about 2.4901721737.

A sufficient record condition is therefore

    (593/2000)delta4
      < E_rec-233/1600-(C_match+C_low)/R.

If the only new arithmetic error is the fourth moment, sufficient ceilings are approximately:

    R=256: mu4(H_R)<3.27663658...
    R=320: mu4(H_R)<3.28319795...
    R=400: mu4(H_R)<3.28844705...
    R=512: mu4(H_R)<3.29304001...
    R=768: mu4(H_R)<3.29850782...
    R=1024: mu4(H_R)<3.30124173...

So the current scalar kill gate is one one-sided fixed-band fourth-moment estimate. At R=400 it is enough to prove mu4(H_R)<3.28844705.... The sine-process target is 3.25.

The Proposition-R firewall remains intact because the quartic is applied only after the original bounded consumer has been reduced to H_R.

See:

    notes/WP84_MATCHED_QUARTIC_MAJORANT.md
    notes/WP71_M3_ARCHIVE_RECONSTRUCTION.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
