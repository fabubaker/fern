/**
 * This file was auto-generated by Fern from our API Definition.
 */
export declare type WeatherReport = "SUNNY" | "CLOUDY" | "RAINING" | "SNOWING";
export declare const WeatherReport: {
    readonly Sunny: "SUNNY";
    readonly Cloudy: "CLOUDY";
    readonly Raining: "RAINING";
    readonly Snowing: "SNOWING";
    readonly _visit: <R>(value: WeatherReport, visitor: WeatherReport.Visitor<R>) => R;
};
export declare namespace WeatherReport {
    interface Visitor<R> {
        sunny: () => R;
        cloudy: () => R;
        raining: () => R;
        snowing: () => R;
        _other: () => R;
    }
}