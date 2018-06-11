[Docs](ft2-index.md) &raquo; [Support API](ft2-toc.md#support-api) &raquo; Computations

-------------------------------

# Computations

## Synopsis

This section contains various functions used to perform computations on 16.16 fixed-float numbers or 2d vectors.

## FT_MulDiv

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_long">FT_Long</a> )
  <b>FT_MulDiv</b>( <a href="../ft2-basic_types/#ft_long">FT_Long</a>  a,
             <a href="../ft2-basic_types/#ft_long">FT_Long</a>  b,
             <a href="../ft2-basic_types/#ft_long">FT_Long</a>  c );
</pre>
</div>


Compute &lsquo;(a*b)/c&rsquo; with maximum accuracy, using a 64-bit intermediate integer whenever necessary.

This function isn't necessarily as fast as some processor specific operations, but is at least completely portable.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The first multiplier.</p>
</td></tr>
<tr><td class="val" id="b">b</td><td class="desc">
<p>The second multiplier.</p>
</td></tr>
<tr><td class="val" id="c">c</td><td class="desc">
<p>The divisor.</p>
</td></tr>
</table>

<h4>return</h4>

The result of &lsquo;(a*b)/c&rsquo;. This function never traps when trying to divide by zero; it simply returns &lsquo;MaxInt&rsquo; or &lsquo;MinInt&rsquo; depending on the signs of &lsquo;a&rsquo; and &lsquo;b&rsquo;.

<hr>

## FT_MulFix

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_long">FT_Long</a> )
  <b>FT_MulFix</b>( <a href="../ft2-basic_types/#ft_long">FT_Long</a>  a,
             <a href="../ft2-basic_types/#ft_long">FT_Long</a>  b );
</pre>
</div>


Compute &lsquo;(a*b)/0x10000&rsquo; with maximum accuracy. Its main use is to multiply a given value by a 16.16 fixed-point factor.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The first multiplier.</p>
</td></tr>
<tr><td class="val" id="b">b</td><td class="desc">
<p>The second multiplier. Use a 16.16 factor here whenever possible (see note below).</p>
</td></tr>
</table>

<h4>return</h4>

The result of &lsquo;(a*b)/0x10000&rsquo;.

<h4>note</h4>

This function has been optimized for the case where the absolute value of &lsquo;a&rsquo; is less than 2048, and &lsquo;b&rsquo; is a 16.16 scaling factor. As this happens mainly when scaling from notional units to fractional pixels in FreeType, it resulted in noticeable speed improvements between versions 2.x and 1.x.

As a conclusion, always try to place a 16.16 factor as the _second_ argument of this function; this can make a great difference.

<hr>

## FT_DivFix

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_long">FT_Long</a> )
  <b>FT_DivFix</b>( <a href="../ft2-basic_types/#ft_long">FT_Long</a>  a,
             <a href="../ft2-basic_types/#ft_long">FT_Long</a>  b );
</pre>
</div>


Compute &lsquo;(a*0x10000)/b&rsquo; with maximum accuracy. Its main use is to divide a given value by a 16.16 fixed-point factor.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The numerator.</p>
</td></tr>
<tr><td class="val" id="b">b</td><td class="desc">
<p>The denominator. Use a 16.16 factor here.</p>
</td></tr>
</table>

<h4>return</h4>

The result of &lsquo;(a*0x10000)/b&rsquo;.

<hr>

## FT_RoundFix

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_RoundFix</b>( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  a );
</pre>
</div>


Round a 16.16 fixed number.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The number to be rounded.</p>
</td></tr>
</table>

<h4>return</h4>

&lsquo;a&rsquo; rounded to the nearest 16.16 fixed integer, halfway cases away from zero.

<h4>note</h4>

The function uses wrap-around arithmetic.

<hr>

## FT_CeilFix

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_CeilFix</b>( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  a );
</pre>
</div>


Compute the smallest following integer of a 16.16 fixed number.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The number for which the ceiling function is to be computed.</p>
</td></tr>
</table>

<h4>return</h4>

&lsquo;a&rsquo; rounded towards plus infinity.

<h4>note</h4>

The function uses wrap-around arithmetic.

<hr>

## FT_FloorFix

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_FloorFix</b>( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  a );
</pre>
</div>


Compute the largest previous integer of a 16.16 fixed number.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>The number for which the floor function is to be computed.</p>
</td></tr>
</table>

<h4>return</h4>

&lsquo;a&rsquo; rounded towards minus infinity.

<hr>

## FT_Vector_Transform

Defined in FT_FREETYPE_H (freetype/freetype.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Vector_Transform</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*        vec,
                       <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>*  matrix );
</pre>
</div>


Transform a single vector through a 2x2 matrix.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="vector">vector</td><td class="desc">
<p>The target vector to transform.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="matrix">matrix</td><td class="desc">
<p>A pointer to the source 2x2 matrix.</p>
</td></tr>
</table>

<h4>note</h4>

The result is undefined if either &lsquo;vector&rsquo; or &lsquo;matrix&rsquo; is invalid.

<hr>

## FT_Matrix_Multiply

Defined in FT_GLYPH_H (freetype/ftglyph.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Matrix_Multiply</b>( <span class="keyword">const</span> <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>*  a,
                      <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>*        b );
</pre>
</div>


Perform the matrix operation &lsquo;b = a*b&rsquo;.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="a">a</td><td class="desc">
<p>A pointer to matrix &lsquo;a&rsquo;.</p>
</td></tr>
</table>

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="b">b</td><td class="desc">
<p>A pointer to matrix &lsquo;b&rsquo;.</p>
</td></tr>
</table>

<h4>note</h4>

The result is undefined if either &lsquo;a&rsquo; or &lsquo;b&rsquo; is zero.

Since the function uses wrap-around arithmetic, results become meaningless if the arguments are very large.

<hr>

## FT_Matrix_Invert

Defined in FT_GLYPH_H (freetype/ftglyph.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_error">FT_Error</a> )
  <b>FT_Matrix_Invert</b>( <a href="../ft2-basic_types/#ft_matrix">FT_Matrix</a>*  matrix );
</pre>
</div>


Invert a 2x2 matrix. Return an error if it can't be inverted.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="matrix">matrix</td><td class="desc">
<p>A pointer to the target matrix. Remains untouched in case of error.</p>
</td></tr>
</table>

<h4>return</h4>

FreeType error code. 0&nbsp;means success.

<hr>

## FT_Angle

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  <span class="keyword">typedef</span> <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  <b>FT_Angle</b>;
</pre>
</div>


This type is used to model angle values in FreeType. Note that the angle is a 16.16 fixed-point value expressed in degrees.

<hr>

## FT_ANGLE_PI

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_ANGLE_PI</b>  ( 180L &lt;&lt; 16 )
</pre>
</div>


The angle pi expressed in <a href="../ft2-computations/#ft_angle">FT_Angle</a> units.

<hr>

## FT_ANGLE_2PI

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_ANGLE_2PI</b>  ( <a href="../ft2-computations/#ft_angle_pi">FT_ANGLE_PI</a> * 2 )
</pre>
</div>


The angle 2*pi expressed in <a href="../ft2-computations/#ft_angle">FT_Angle</a> units.

<hr>

## FT_ANGLE_PI2

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_ANGLE_PI2</b>  ( <a href="../ft2-computations/#ft_angle_pi">FT_ANGLE_PI</a> / 2 )
</pre>
</div>


The angle pi/2 expressed in <a href="../ft2-computations/#ft_angle">FT_Angle</a> units.

<hr>

## FT_ANGLE_PI4

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
#<span class="keyword">define</span> <b>FT_ANGLE_PI4</b>  ( <a href="../ft2-computations/#ft_angle_pi">FT_ANGLE_PI</a> / 4 )
</pre>
</div>


The angle pi/4 expressed in <a href="../ft2-computations/#ft_angle">FT_Angle</a> units.

<hr>

## FT_Sin

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_Sin</b>( <a href="../ft2-computations/#ft_angle">FT_Angle</a>  angle );
</pre>
</div>


Return the sinus of a given angle in fixed-point format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The input angle.</p>
</td></tr>
</table>

<h4>return</h4>

The sinus value.

<h4>note</h4>

If you need both the sinus and cosinus for a given angle, use the function <a href="../ft2-computations/#ft_vector_unit">FT_Vector_Unit</a>.

<hr>

## FT_Cos

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_Cos</b>( <a href="../ft2-computations/#ft_angle">FT_Angle</a>  angle );
</pre>
</div>


Return the cosinus of a given angle in fixed-point format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The input angle.</p>
</td></tr>
</table>

<h4>return</h4>

The cosinus value.

<h4>note</h4>

If you need both the sinus and cosinus for a given angle, use the function <a href="../ft2-computations/#ft_vector_unit">FT_Vector_Unit</a>.

<hr>

## FT_Tan

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_Tan</b>( <a href="../ft2-computations/#ft_angle">FT_Angle</a>  angle );
</pre>
</div>


Return the tangent of a given angle in fixed-point format.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The input angle.</p>
</td></tr>
</table>

<h4>return</h4>

The tangent value.

<hr>

## FT_Atan2

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-computations/#ft_angle">FT_Angle</a> )
  <b>FT_Atan2</b>( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  x,
            <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>  y );
</pre>
</div>


Return the arc-tangent corresponding to a given vector (x,y) in the 2d plane.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="x">x</td><td class="desc">
<p>The horizontal vector coordinate.</p>
</td></tr>
<tr><td class="val" id="y">y</td><td class="desc">
<p>The vertical vector coordinate.</p>
</td></tr>
</table>

<h4>return</h4>

The arc-tangent value (i.e. angle).

<hr>

## FT_Angle_Diff

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-computations/#ft_angle">FT_Angle</a> )
  <b>FT_Angle_Diff</b>( <a href="../ft2-computations/#ft_angle">FT_Angle</a>  angle1,
                 <a href="../ft2-computations/#ft_angle">FT_Angle</a>  angle2 );
</pre>
</div>


Return the difference between two angles. The result is always constrained to the ]-PI..PI] interval.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle1">angle1</td><td class="desc">
<p>First angle.</p>
</td></tr>
<tr><td class="val" id="angle2">angle2</td><td class="desc">
<p>Second angle.</p>
</td></tr>
</table>

<h4>return</h4>

Constrained value of &lsquo;value2-value1&rsquo;.

<hr>

## FT_Vector_Unit

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Vector_Unit</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  vec,
                  <a href="../ft2-computations/#ft_angle">FT_Angle</a>    angle );
</pre>
</div>


Return the unit vector corresponding to a given angle. After the call, the value of &lsquo;vec.x&rsquo; will be &lsquo;cos(angle)&rsquo;, and the value of &lsquo;vec.y&rsquo; will be &lsquo;sin(angle)&rsquo;.

This function is useful to retrieve both the sinus and cosinus of a given angle quickly.

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="vec">vec</td><td class="desc">
<p>The address of target vector.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The input angle.</p>
</td></tr>
</table>

<hr>

## FT_Vector_Rotate

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Vector_Rotate</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  vec,
                    <a href="../ft2-computations/#ft_angle">FT_Angle</a>    angle );
</pre>
</div>


Rotate a vector by a given angle.

<h4>inout</h4>
<table class="fields">
<tr><td class="val" id="vec">vec</td><td class="desc">
<p>The address of target vector.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The input angle.</p>
</td></tr>
</table>

<hr>

## FT_Vector_Length

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a> )
  <b>FT_Vector_Length</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  vec );
</pre>
</div>


Return the length of a given vector.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="vec">vec</td><td class="desc">
<p>The address of target vector.</p>
</td></tr>
</table>

<h4>return</h4>

The vector length, expressed in the same units that the original vector coordinates.

<hr>

## FT_Vector_Polarize

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Vector_Polarize</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  vec,
                      <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>   *length,
                      <a href="../ft2-computations/#ft_angle">FT_Angle</a>   *angle );
</pre>
</div>


Compute both the length and angle of a given vector.

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="vec">vec</td><td class="desc">
<p>The address of source vector.</p>
</td></tr>
</table>

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="length">length</td><td class="desc">
<p>The vector length.</p>
</td></tr>
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The vector angle.</p>
</td></tr>
</table>

<hr>

## FT_Vector_From_Polar

Defined in FT_TRIGONOMETRY_H (freetype/fttrigon.h).

<div class = "codehilite">
<pre>
  FT_EXPORT( <span class="keyword">void</span> )
  <b>FT_Vector_From_Polar</b>( <a href="../ft2-basic_types/#ft_vector">FT_Vector</a>*  vec,
                        <a href="../ft2-basic_types/#ft_fixed">FT_Fixed</a>    length,
                        <a href="../ft2-computations/#ft_angle">FT_Angle</a>    angle );
</pre>
</div>


Compute vector coordinates from a length and angle.

<h4>output</h4>
<table class="fields">
<tr><td class="val" id="vec">vec</td><td class="desc">
<p>The address of source vector.</p>
</td></tr>
</table>

<h4>input</h4>
<table class="fields">
<tr><td class="val" id="length">length</td><td class="desc">
<p>The vector length.</p>
</td></tr>
<tr><td class="val" id="angle">angle</td><td class="desc">
<p>The vector angle.</p>
</td></tr>
</table>

<hr>

