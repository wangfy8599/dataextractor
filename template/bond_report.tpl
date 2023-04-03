<!DOCTYPE html>
<html>
      
<head>
      
    <!-- CSS style to set alternate table 
            row using color -->
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
          
        th, td {
            text-align: left;
            padding: 3px;
        }
          
        tr:nth-child(even) {
            background-color: #dcdcdc;
        }
        
        tr:hover {
            background-color: LightSkyBlue;
            cursor: pointer;
        }
    </style>
</head>
  
<body>

<h3>我的持仓 (低溢价)</h3>
<%table_place_holder_0%>

<h3>我的持仓 (双低排序)</h3>
<%table_place_holder_2%>

<h3>我的待选</h3>
<%table_place_holder_3%>

<h3>辰星双低 - Top 30</h3>
<%table_place_holder_1%>

<h3>我的持仓 (辰星三低)</h3>
<%table_place_holder_4%>

<h3>我的待选 (辰星三低)</h3>
<%table_place_holder_5%>

<h3>(辰星三低) - Top 30</h3>
<%table_place_holder_6%>

<h3>税前收益率</h3>
<%table_place_holder_7%>

<h3>股价高</h3>
<%table_place_holder_8%>

<h3>转债余额</h3>
<%table_place_holder_9%>

<h3>我的持仓 (剩余年限)</h3>
<%table_place_holder_10%>

</body>
  
</html>