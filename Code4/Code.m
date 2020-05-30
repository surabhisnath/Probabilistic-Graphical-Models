%%%Code to estimate the value of pi using Monte Carlo
%%%Kindly note: code can take a little time for all 3 plots to be created
%%%Plots and results have also been presented in the pdf report

n = [1e2 1e3 1e4];                      %total number of randomly generated points
for i=1:length(n)       
    for j=1:n(i)
        x = rand(j,1);                  %generating x-coordinates
        y = rand(j,1);                  %generating y-coordinates
    end
    hypot_sq = x.^2+y.^2;
    check_in_quadrant = hypot_sq<1;     %boolean vector to check if generated points are within quadrant
    pi_est = 4*sum(check_in_quadrant(:,1))/n(i);    %estimating value of pi
    
    %Displaying Result
    fprintf('With %d randomly generated points, the approximated value of pi is %.4f\n',n(i),pi_est);
    
    %Visualizing Result
    h = figure;
    ax = axes();
    hold on;
    ax.XLim = [0 1];
    ax.YLim = [0 1];
    axis equal;
    caption_title = sprintf('N = %d', n(i));
    title(caption_title);
    for j=1:n(i)
        if(check_in_quadrant(j,1)==1)
            scatter(x(j,1),y(j,1),'b.');        %Points inside the quadrant are in blue
        else
            scatter(x(j,1),y(j,1),'r.');        %Points outside the quadrant are in red
        end
    end
    fig_title = sprintf('N_%d.png',n(i));
    saveas(h,fig_title);
end